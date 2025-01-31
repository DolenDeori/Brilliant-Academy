from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import authenticate
from django.forms import fields
from accounts.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required add a valid email Address')

    # trying

    class Meta:
        model = Account
        fields = ('email', 'firstname', 'lastname', "password1", "password2", "phone")


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')
    

    def clean(self):

        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('invalid email or password')
