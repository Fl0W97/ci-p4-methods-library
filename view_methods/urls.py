from . import views
from django.urls import path
from .views import MethodList, method_page, method_create

urlpatterns = [
    path('', views.MethodList.as_view(), name='home'),
    path('create/', method_create, name='method_creation'),
    path('<slug:slug>/', views.method_page, name='method_page'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]