from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2']

