from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, 'app/index.html')


def error404(request, exception):
    return HttpResponse('<b>404</b>')
