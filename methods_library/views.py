from django.shortcuts import render

def custom_page_not_found(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, '404.html', status=404)
