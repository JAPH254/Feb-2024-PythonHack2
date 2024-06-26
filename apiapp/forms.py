from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import user

class CustomUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = user
    fields = ('username', 'email', 'password1', 'password2')