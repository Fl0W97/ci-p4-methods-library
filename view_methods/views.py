from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Method, Comment, Like, About
from .forms import CommentForm, MethodForm, AboutForm
from django.db.models import Count
from django.contrib.auth.models import User


# Displays an all approved methods, index.html
class MethodList(generic.ListView):
    """ queryset = Method.objects.all() """
    template_name = "view_methods/index.html"
    paginate_by = 9  # Show 9 methods per page

    def get_queryset(self):
        # Start with all Method objects
        queryset = Method.objects.filter(status=1)

        # Get parameters from the URL query string
        purpose = self.request.GET.get('purpose')
        duration = self.request.GET.get('duration')
        location = self.request.GET.get('location')

        # Filter by purpose
        if purpose:
            queryset = queryset.filter(purpose=purpose)

        # Filter by duration
        if duration:
            queryset = queryset.filter(duration=duration)

        # Filter by location
        if location:
            queryset = queryset.filter(location=location)

        # Annotate each method with the number of likes (using name 'likes')
        queryset = queryset.annotate(like_count=Count('likes'))

        # Order by the number of likes, descending
        queryset = queryset.order_by('-like_count')

        return queryset


# Displays an individual method, method_page.html
def method_page(request, slug):
    # Filter methods by status and get the method based on the slug
    queryset = Method.objects.filter(status=1)
    method = get_object_or_404(queryset, slug=slug)

    # Annotate the method with the number of likes
    method = Method.objects.annotate(
        like_count=Count('likes')
    ).get(id=method.id)

    # Get all comments for the method and count approved comments
    comments = method.comments.all().order_by("-created_on")
    comment_count = method.comments.filter(approved=True).count()

    # Check if the user has already liked the method
    # Default value if the user is not authenticated
    user_liked_method = False

    if request.user.is_authenticated:
        # Check if the user has already liked this method
        user_liked_method = Like.objects.filter(
            user=request.user, method=method
        ).exists()

    # Handle like functionality when the button is clicked
    if request.method == "POST":
        if request.user.is_authenticated and not user_liked_method:
            # Create a new Like object if not already liked
            Like.objects.create(user=request.user, method=method)
            messages.add_message(
                request, messages.SUCCESS, 'You liked this method!'
            )

            # Re-fetch to update the like count and liked status
            user_liked_method = True

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
    method = Method.objects.annotate(
        like_count=Count('likes')
    ).get(id=method.id)

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


# view to edit comments, method_page.html
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
            messages.add_message(
                request, messages.SUCCESS, 'Comment is updated'
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('method_page', args=[slug]))


# view to delete comment, method_page.html
def comment_delete(request, slug, comment_id):

    queryset = Method.objects.filter(status=1)
    method = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Comment deleted.'
        )
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments.'
        )

    return HttpResponseRedirect(reverse('method_page', args=[slug]))


# Handle method creation and submission, method_creation.html
def method_create(request):

    if not request.user.is_authenticated:
        # If the user is not authenticated, redirect them to the login page
        messages.add_message(
            request, messages.ERROR, 'You must be logged in'
                                     ' to create a method.'
        )
        return HttpResponseRedirect(reverse('home'))

    if request.method == "POST":
        method_form = MethodForm(request.POST, request.FILES)
        if method_form.is_valid():
            method = method_form.save(commit=False)
            method.author = request.user  # Link method to the current user
            method.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Your method has been submitted and is pending approval')

            # Redirect to the homepage after successful submission
            return HttpResponseRedirect(reverse('home'))

    else:
        # Instantiate a blank form if it's a GET request
        method_form = MethodForm()

    return render(
        request,
        # Template where the form will be rendered
        'view_methods/method_creation.html',
        {'method_form': method_form}
    )


# Displays users's content, private_collection.html
# no ListView, it has to be a TemplateView
class PrivateCollectionView(generic.TemplateView):
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


class AboutPageView(generic.TemplateView):
    template_name = 'view_methods/about.html'

    def get_context_data(self, **kwargs):
        # Call the parent method to get the default context
        context = super().get_context_data(**kwargs)

        # Fetch the 'About' object
        about = About.objects.first()
        context['about'] = about

        return context
