from django import forms

from contact_module.models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['fullName', 'title', 'email', 'message']
        widgets = {
            'fullName': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }), 'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان'
            }), 'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }), 'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'پیغام',
                'id': 'message'
            }),
        }
        labels = {
            'fullName': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'title': 'عنوان',
            'message': 'پیغام'
        }
