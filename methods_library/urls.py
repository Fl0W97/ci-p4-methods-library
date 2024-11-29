from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from methods_library import views

handler404 = 'methods_library.views.custom_page_not_found'
handler500 = 'methods_library.views.internal_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path("", include("view_methods.urls"), name="view_methods-urls"),
]
