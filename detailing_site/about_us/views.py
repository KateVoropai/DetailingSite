from django.shortcuts import render
from .models import Category, Price

def index(request):
    return render(request, 'about_us/index.html')

def price(request):
    price = Price.objects.all()
    return render(request, 'about_us/price.html', {
        'price':price
    })
