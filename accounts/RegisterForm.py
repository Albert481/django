from django import forms
from django.contrib.auth import (authenticate, get_user_model, login, logout)
import re
from accounts.models import Auth_User

class UserRegisterForm(forms.ModelForm):
    # retrieves variables
    email = forms.CharField(max_length=255, label='Email Address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    email2 = forms.CharField(max_length=255, label='Repeat Email Address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = Auth_User
        fields = ('email',
                  'email2',
                  'password',
                  'password2')

    def clean_email2(self):
        #Check if 2 emails match
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails do not match")
        return email2

    def clean_password2(self):
        #Check if 2 passwords match
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords do not match")

        # regex to ensure that password fits minimum requirements
        password_regex = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}")
        m = password_regex.match(password)

        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        if m:
            print(m)
            return password2
        else:
            print(m)
            raise forms.ValidationError(
                "Please ensure that your password contains at least 8 characters, with at least 1 uppercase letter, 1 lowercase letter and 1 number")


    def save(self, commit=True):
        #Save password in hash
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        print(user)
        if commit:
            user.save()
        return user