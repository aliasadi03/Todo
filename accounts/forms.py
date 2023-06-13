from django import forms
from . import models

class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(min_length=4, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(min_length=4, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class ResetPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

class PasswordChangeForm(forms.Form):
    password = forms.CharField(min_length=4, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirmpassword = forms.CharField(min_length=4, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))