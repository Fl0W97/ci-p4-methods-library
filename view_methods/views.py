from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Method, Comment, Like
from .forms import CommentForm, MethodForm


# Create your views here.
class MethodList(generic.ListView):
    """ queryset = Method.objects.all() """
    template_name = "view_methods/index.html"
    paginate_by = 8  # Show 8 methods per page

    def get_queryset(self):
        queryset = Method.objects.all() # Start with all Method objects
        
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
        
        return queryset
        

#Display an individual :model:view_methods.method; template:`view_methods/method_page.html`
def method_page(request, slug):

    queryset = Method.objects.filter(status=1)
    method = get_object_or_404(queryset, slug=slug)
    comments = method.comments.all().order_by("-created_on")
    comment_count = method.comments.filter(approved=True).count()

    # Handle like functionality when the POST request is made (when the like button is clicked)
    if request.method == "POST":
        # Handle liking a method
        if request.user.is_authenticated:
            # Check if the user has already liked this method
            existing_like = Like.objects.filter(user=request.user, method=method)
            if not existing_like.exists():
                # Create a new Like object
                Like.objects.create(user=request.user, method=method)
                messages.add_message(request, messages.SUCCESS, 'You liked this method!')
            else:
                messages.add_message(request, messages.INFO, 'You have already liked this method.')

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

    return render(
        request,
        "view_methods/method_page.html",
        {
            "method": method,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
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
        method_form = MethodForm(request.POST)
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