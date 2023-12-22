from django.shortcuts import render

def error_500(request, exception):
    data = {}
    return render(request, 'error_html/500.html', status=500)

def error_405(request, exception):
    data = {}
    return render(request, 'error_html/405.html', status=405)

def error_404(request, exception):
    data = {}
    return render(request, 'error_html/404.html', status=404)

def error_403(request, exception):
    data = {}
    return render(request, 'error_html/403.html', status=403)