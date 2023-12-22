from django.shortcuts import render

def error_404(request, exception):
    data = {}
    return render(request, 'error_html/404.html', status=404)

def error_403(request, exception):
    data = {}
    return render(request, 'error_html/403.html', status=403)