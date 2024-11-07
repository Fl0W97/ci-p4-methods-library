from django.shortcuts import render
from django.views import generic
from .models import Method


# Create your views here.
class MethodList(generic.ListView):
    queryset = Method.objects.all()
    template_name = "view_methods/index.html"