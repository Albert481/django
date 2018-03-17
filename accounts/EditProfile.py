from django import forms
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from accounts.models import Profile

User = get_user_model()

class UserProfile(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Change New Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm New Password')

    class Meta:
        model = User
        fields = [
            'password',
            'password2'
        ]
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords must match")
        return password

class EditValues(forms.ModelForm):
    ethaddress = forms.CharField(max_length=255, label='Ethaddress', widget=forms.TextInput(attrs={'id': 'eth_value','class': 'text-right, form-control', 'required': False}))
    indicativecontribution = forms.CharField(max_length=255, label='Indicative Contribution', widget=forms.NumberInput(attrs={'id': 'ind_value', 'class': 'text-right, form-control', 'required': False}))

    class Meta:
        model = Profile
        fields = [
            'ethaddress',
            'indicativecontribution'
        ]
        widgets = {'tag': forms.HiddenInput()}