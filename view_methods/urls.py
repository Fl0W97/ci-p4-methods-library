from . import views
from django.urls import path
from .views import MethodList, method_page

urlpatterns = [
    path('', views.MethodList.as_view(), name='home'),
    path('<slug:slug>/', views.method_page, name='method_page'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]