from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100, null=True)
    cnpj = models.CharField(max_length=14, null=True)
    address = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    phone = models.CharField(max_length=11, null=True)
    reviews = models.IntegerField(null=True, default=0)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

FOOD_OPTIONS = (
    ('Lanche', 'Lanche'),
    ('Prato', 'Prato'),
    ('Pizza', 'Pizza'),
    ('Doce', 'Doce'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    category = models.CharField(max_length=50, choices=FOOD_OPTIONS, null=True)
    price = models.FloatField(null=True)
    photo = models.ImageField(null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=False, null=True)
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True)

    def __str__(self):
        return self.id

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True)
    
    def __str__(self):
        return self.product