from django.contrib import admin
from .models import Method, Comment, About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Method)
class MethodAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'purpose')
    search_fields = ['title', 'author']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('summary', 'instructions', 'material')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('author', 'body',)
    search_fields = ['author', 'body']
    list_filter = ('author', 'approved', 'method')


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title',)
    summernote_fields = ('body',)
