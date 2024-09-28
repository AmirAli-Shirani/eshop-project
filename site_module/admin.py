from django.contrib import admin

from site_module import models


# Register your models here.
class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'position']
    list_editable = ['url', 'position']


class SiteSliderAdmin(admin.ModelAdmin):
    list_display = ['sub_title', 'image','is_active']
    list_editable = ['sub_title', 'image','is_active']


admin.site.register(models.SiteSettings)
admin.site.register(models.SiteSlider)
admin.site.register(models.SiteBanner, SiteBannerAdmin)
