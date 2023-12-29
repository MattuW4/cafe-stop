from django.shortcuts import render

def error_500(request):
    """
    Custom 500 page
    """
    data = {}
    return render(request, 'error_html/500.html', status=500)

def error_405(request, exception):
    """
    Custom 405 page
    """
    data = {}
    return render(request, 'error_html/405.html', status=405)

def error_404(request, exception):
    """
    Custom 400 page
    """
    data = {}
    return render(request, 'error_html/404.html', status=404)

def error_403(request, exception):
    """
    Custom 403 page
    """
    data = {}
    return render(request, 'error_html/403.html', status=403)