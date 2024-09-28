from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView

from contact_module.forms import ContactUsModelForm
from contact_module.models import ContactUs


# Create your views here.

# class ContactUsView(View):
#     def get(self, request):
#         contact_form = ContactUsModelForm()
#         return render(request, 'contact_module/contact-us.html', {
#             'contact_form': contact_form
#         })
#
#     def post(self, request):
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('home_page')
#         return render(request, 'contact_module/contact-us.html', {
#             'contact_form': contact_form
#         })

class ContactUsView(CreateView):
    template_name = 'contact_module/contact-us.html'
    form_class = ContactUsModelForm
    success_url = reverse_lazy('home_page')
