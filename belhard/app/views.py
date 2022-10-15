from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Category, Product
from .forms import Calculator, FeedbackForm


mixin = {
    'facebook': 'https://facebook.com',
    'twitter': 'https://twitter.com',
    'brand_name': 'BelHard'
}


def index(request: HttpRequest):
    categories = Category.objects.all().order_by('-name')
    products = Product.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'app/index.html', {
        'categories': categories,
        'products': products,
        'feedback_form': FeedbackForm()
    } | mixin)


def error404(request, exception):
    return HttpResponse('<b>404</b>')
