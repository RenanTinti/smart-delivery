from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):

    restaurants = Restaurant.objects.all()

    context = {
        'restaurants': restaurants,
    }

    return render(request, 'index.html', context)

def menu(request, pk):

    restaurant = Restaurant.objects.get(id=pk)
    menu = Product.objects.filter(restaurant=pk)

    context = {
        'restaurant': restaurant,
        'menu': menu,
    }

    return render(request, 'menu.html', context)

def product(request, pk_restaurant, pk_product):

    product = Product.objects.get(restaurant=pk_restaurant, id=pk_product)

    context = {
        'product': product,
    }

    return render(request, 'product.html', context)