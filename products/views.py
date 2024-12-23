from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Product
from django.core.exceptions import PermissionDenied  
from django.contrib.auth.decorators import login_required 

# Create your views here.

# @login_required 
def product(request, name):
    print(name)
    print(Product.objects.get(id=name))
    try:
        data = Product.objects.get(id=name)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'products/product.html' ,{'product': data} )


def products(request):
    data = Product.objects.all()
    # data.filter(name__contains='app') // srearch
    # data.filter(name__exact='lina')
    # data.filter(price__in=[100, 200])
    # data.filter(price__range=[10, 500])
    # if request.user.is_anonymous(): 
    #     raise PermissionDenied()
    return render(request , 'products/products.html' , {'products': data.order_by('name')})