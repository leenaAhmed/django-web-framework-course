from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

def product(request):
    return render(request , 'products/product.html')


def products(request):
    data = Product.objects.all()
    # data.filter(name__contains='app') // srearch
    # data.filter(name__exact='lina')
    # data.filter(price__in=[100, 200])
    # data.filter(price__range=[10, 500])

    return render(request , 'products/products.html' , {'products': data.order_by('name')})