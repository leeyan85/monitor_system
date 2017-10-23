#-*- coding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="domain username",
        error_messages={'required': 'please input the username'},
        widget=forms.TextInput(
            attrs={
                'placeholder':"your email address prefix",
                'class':"form-control span12"
            }
        ),
    )    
    password = forms.CharField(
        required=True,
        label="domain password",
        error_messages={'required': 'please input password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':"your email password",
                'class':"form-controlspan12 form-control"
            }
        ),
    )  
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("user name and password are required")
        else:
            cleaned_data = super(LoginForm, self).clean()
