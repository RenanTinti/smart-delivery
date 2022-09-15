from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100, null=True)
    cnpj = models.CharField(max_length=14, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    phone = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.name

FOOD_OPTIONS = (
    ('Lanche', 'Lanche'),
    ('Prato', 'Prato'),
    ('Pizza', 'Pizza'),
    ('Doce', 'Doce'),
)

class Food(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    category = models.CharField(max_length=50, choices=FOOD_OPTIONS, null=True)
    price = models.FloatField(null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name