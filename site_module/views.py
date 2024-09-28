from django.views.generic import TemplateView

from .models import SiteSettings, SiteSlider


# Create your views here.
class AboutUsView(TemplateView):
    template_name = 'site_module/about-us-page.html'

    def get_context_data(self, **kwargs):
        site_setting = SiteSettings.objects.get()
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['setting'] = site_setting
        return context


# class SiteSliderView(TemplateView):
#     template_name = 'home_module/index-page.html'
#
#     def get_context_data(self, **kwargs):
#         site_slider = SiteSlider.objects.filter(is_active=True)
#         context = super().get_context_data()
#         context['site_slider'] = site_slider
#         return context
