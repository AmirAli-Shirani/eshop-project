from django.views.generic import CreateView, ListView

from .forms import ContactUsModelForm
from .models import UserProfile


class ContactUsFormView(CreateView):
    template_name = 'contact_module/contact-us-page.html'
    form_class = ContactUsModelForm
    success_url = '/products/'


class CreateProfileView(CreateView):
    template_name = 'contact_module/create-profile-page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/profile-page'


class ProfilePage(ListView):
    template_name = 'contact_module/profile-page.html'
    model = UserProfile
    context_object_name = 'profiles'
