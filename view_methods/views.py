from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Method


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

    return render(
        request,
        "view_methods/method_page.html",
        {"method": method},
    )