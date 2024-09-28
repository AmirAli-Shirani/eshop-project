from django.contrib import admin

from contact_module.models import ContactUs


# Register your models here.
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'title' , 'is_read_by_admin']
    list_editable = ['is_read_by_admin']