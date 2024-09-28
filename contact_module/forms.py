from django import forms

from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),

            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message'
            })
        }
        labels = {
            'full_name': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'title': 'عنوان',
            'message': 'متن پیام',
        }
        error_messages = {
            'full_name': {
                'required': 'نامو نام خانوادگی اجباری می باشد لطفا وارد نمایید'
            },
            'email': {
                'required': 'لطفا ایمیل خود را درست وارد نمایید'
            },
            'title': {
                'required': 'لطفا عنوان خود را درست وارد نمایید'
            },
            'message': {
                'required': 'لطفا متن پیام خود را درست وارد نمایید'
            },
        }


class ProfileForm(forms.Form):
    user_image = forms.ImageField()
