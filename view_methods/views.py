from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Method, Comment, Like, About
from .forms import CommentForm, MethodForm, AboutForm
from django.db.models import Count
from django.contrib.auth.models import User


# Create your views here.
class MethodList(generic.ListView):
    """ queryset = Method.objects.all() """
    template_name = "view_methods/index.html"
    paginate_by = 9  # Show 9 methods per page

    def get_queryset(self):
        queryset = Method.objects.filter(status=1) # Start with all Method objects
        
        # Filter by purpose (if specified)
        purpose = self.request.GET.get('purpose') # Get the 'purpose' parameter from the URL query string
        duration = self.request.GET.get('duration') # Get the 'duration' parameter from the URL query string
        location = self.request.GET.get('location') # Get the 'purpose' parameter from the URL query string

        # Filter by purpose
        if purpose:
            queryset = queryset.filter(purpose=purpose)

        # Filter by duration
        if duration:
            queryset = queryset.filter(duration=duration)

        # Filter by location
        if location:
            queryset = queryset.filter(location=location)

        # Annotate each method with the number of likes (using the related name 'likes')
        queryset = queryset.annotate(like_count=Count('likes'))

        # Order by the number of likes, descending
        queryset = queryset.order_by('-like_count')
        
        return queryset
        

#Displays an individual :model:view_methods.method; template:`view_methods/method_page.html`
def method_page(request, slug):
    # Filter methods by status and get the method based on the slug
    queryset = Method.objects.filter(status=1)
    method = get_object_or_404(queryset, slug=slug)

    # Annotate the method with the number of likes
    method = Method.objects.annotate(like_count=Count('likes')).get(id=method.id)

    # Get all comments for the method and count approved comments
    comments = method.comments.all().order_by("-created_on")
    comment_count = method.comments.filter(approved=True).count()

    # Check if the user has already liked the method
    user_liked_method = False  # Default value in case the user is not authenticated

    if request.user.is_authenticated:
        # Check if the user has already liked this method
        user_liked_method = Like.objects.filter(user=request.user, method=method).exists()

    # Handle like functionality when the POST request is made (when the like button is clicked)
    if request.method == "POST":
        if request.user.is_authenticated and not user_liked_method:
            # Create a new Like object if not already liked
            Like.objects.create(user=request.user, method=method)
            messages.add_message(request, messages.SUCCESS, 'You liked this method!')

            # Re-fetch to update the like count and liked status
            user_liked_method = True  # Since the user just liked the method

        # Handle comment submission
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.method = method
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been submitted and is pending approval'
            )

    comment_form = CommentForm()

    # Refresh the method object to include the updated like_count
    method = Method.objects.annotate(like_count=Count('likes')).get(id=method.id)


    return render(
        request,
        "view_methods/method_page.html",
        {
            "method": method,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "user_liked_method": user_liked_method,
        },
    )


#view to edit comments
def comment_edit(request, slug, comment_id):

    if request.method == "POST":

        queryset = Method.objects.filter(status=1)
        method = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.method = method
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment is updated')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('method_page', args=[slug]))


#view to delete comment
def comment_delete(request, slug, comment_id):

    queryset = Method.objects.filter(status=1)
    method = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted.')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments.')

    return HttpResponseRedirect(reverse('method_page', args=[slug]))


# Handle method creation and submission
def method_create(request):

    if not request.user.is_authenticated:
        # If the user is not authenticated, redirect them to the login page
        messages.add_message(request, messages.ERROR, 'You must be logged in to create a method.')
        return HttpResponseRedirect(reverse('home'))

    if request.method == "POST":
        method_form = MethodForm(request.POST, request.FILES)
        if method_form.is_valid():
            method = method_form.save(commit=False)
            method.author = request.user    # Link method to the current user
            method.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Your method has been submitted and is pending approval')

            # Redirect to the method list page or another page after successful submission
            return HttpResponseRedirect(reverse('home'))

    else:
        method_form = MethodForm()     # Instantiate a blank form if it's a GET request

    return render(
        request,
        'view_methods/method_creation.html',  # Template where the form will be rendered
        {'method_form': method_form}
    )


"""class MethodPrivateCollection(generic.ListView):
    queryset = Method.objects.all()
    template_name = "view_methods/private_collection.html"
    paginate_by = 8  # Show 8 methods per page

    def get_queryset(self):
        queryset = Method.objects.filter(author=self.request.user) # only the user's method should be displayed
        
        return queryset"""


"""class CommentPrivateCollection(generic.ListView):
    queryset = Method.objects.all()
    template_name = "view_methods/private_collection.html"
    paginate_by = 8  # Show 8 methods per page

    def get_queryset(self):
        queryset = Comment.objects.filter(author=self.request.user) # only the user's comments should be displayed
        
        return queryset"""


class PrivateCollectionView(generic.TemplateView):  # no List view, it has to be a TemplateView, since I am using twow different databases
    template_name = "view_methods/private_collection.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch methods created by the logged-in user
        methods = Method.objects.filter(author=self.request.user)
        context['method_list'] = methods

        # Fetch comments created by the logged-in user
        comments = Comment.objects.filter(author=self.request.user)
        context['comment_list'] = comments

        # Fetch comments created by the logged-in user
        liked_methods = Method.objects.filter(likes__user=self.request.user)
        context['liked_methods'] = liked_methods

        return context


"""
from django.shortcuts import render
from .models import Method, Comment

def user_collection(request):
    # Get all methods created by the logged-in user
    method_list = Method.objects.filter(author=request.user)
    
    # Get all comments created by the logged-in user
    comment_list = Comment.objects.filter(author=request.user)
    
    return render(request, 'view_methods/private_collection.html', {
        'method_list': method_list,
        'comment_list': comment_list
    })
"""

"""
def about(request):
    return render(request, 'view_methods/about.html') """
    

class AboutPageView(generic.TemplateView):
    template_name = 'view_methods/about.html'

    def get_context_data(self, **kwargs):
        # Call the parent method to get the default context
        context = super().get_context_data(**kwargs)

        # Fetch the 'About' object (assuming there's only one About instance)
        about = About.objects.first()
        context['about'] = about
        return context