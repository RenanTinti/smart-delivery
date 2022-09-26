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
    menu = Food.objects.filter(restaurant=pk)

    context = {
        'restaurant': restaurant,
        'menu': menu,
    }

    return render(request, 'menu.html', context)