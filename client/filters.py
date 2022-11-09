import django_filters
from django_filters import CharFilter
from .models import *

class RestaurantFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    district = CharFilter(field_name='district', lookup_expr='icontains')
    city = CharFilter(field_name='city', lookup_expr='icontains')

    class Meta:
        model = Restaurant
        fields = ['name', 'district', 'city']