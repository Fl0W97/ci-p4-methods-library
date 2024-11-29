from django.shortcuts import render

def custom_page_not_found(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, '404.html', status=404)

def internal_error(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, '500.html', status=500)
