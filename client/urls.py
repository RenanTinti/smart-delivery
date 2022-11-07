
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('menu/<int:pk>', menu, name='menu'),
    path('product/<int:pk_restaurant>/<int:pk_product>', product, name='product'),
]