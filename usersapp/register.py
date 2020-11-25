from django import forms
from django.contrib.auth.forms import UserCreationForm
# import model User
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]


# updating user - modelforms
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # here v just update the email and username fields.
    class Meta:
        model = User
        fields = ['username', 'email']


# updating profile image so create a new form that inherits model form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
