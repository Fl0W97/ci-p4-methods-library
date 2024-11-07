from . import views
from django.urls import path

urlpatterns = [
    path('', views.MethodList.as_view(), name='home'),
]