from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    email = forms.EmailField(label='آدرس ایمیل :', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='نام :', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='نام خانوادگی', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='رمز عبور :', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label='تکرار رمز عبور :',
                                       widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('کلمه عبور و تکرار آن مغایرت دارند')


class LoginForm(forms.Form):
    email = forms.EmailField(label='آدرس ایمیل :', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='رمز عبور :', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
