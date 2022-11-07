from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# UserCreationForm is a django class for user creation. CreateUserForm is a class that inherit from UserCreationForm, so we can edit it. The CreateUserForm is the one we will be using in the views
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
