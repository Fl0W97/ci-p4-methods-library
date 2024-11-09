from django.contrib import admin
from .models import Method, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Method)
class MethodAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'purpose')
    search_fields = ['title','author']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('summary','instructions','material')


# Register your models here.
admin.site.register(Comment)