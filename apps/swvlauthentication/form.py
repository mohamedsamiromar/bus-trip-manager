from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.swvlauthentication.models import Profile


class SignUpForm(UserCreationForm):
    age = forms.FloatField()
    phone_number = forms.CharField(max_length=11)

    class Meta:
        model = User
        fields = ('age', 'phone_number', 'username', 'first_name', 'last_name', 'email')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'birthday')