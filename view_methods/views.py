from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Method
from .forms import CommentForm


# Create your views here.
class MethodList(generic.ListView):
    queryset = Method.objects.all()
    template_name = "view_methods/index.html"

def method_page(request, slug):
    """
    Display an individual :model:`view_methods.method`.

    **Context**

    ``method``
        An instance of :model:`view_methods.method`.

    **Template:**

    :template:`view_methods/method_page.html`
    """

    queryset = Method.objects.filter(status=1)
    method = get_object_or_404(queryset, slug=slug)
    comments = method.comments.all().order_by("-created_on")
    comment_count = method.comments.filter(approved=True).count()
    if request.method == "POST":
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