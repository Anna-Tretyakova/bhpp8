from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Category, Product
from .forms import Calculator


mixin = {
    'facebook': 'https://facebook.com',
    'twitter': 'https://twitter.com'
}


def index(request: HttpRequest):
    categories = Category.objects.all().order_by('-name')
    products = Product.objects.all()
    return render(request, 'app/index.html', {
        'categories': categories,
        'menu': ['Menu 1', 'Menu 2'],
        'products': products
    } | mixin)


def index2(request):
    return render(request, 'app/index2.html', mixin | {'calculator_form': Calculator()})


def error404(request, exception):
    return HttpResponse('<b>404</b>')
