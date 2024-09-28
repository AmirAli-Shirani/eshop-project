from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView
from product_module.models import Product, ProductCategory
from site_module.models import SiteSlider
from utils.convertors import group_list


# Create your views here.
class HomePage(TemplateView):
    template_name = 'home_module/index-page.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:12]
        context['latest_products'] = group_list(latest_products)
        site_slider = SiteSlider.objects.filter(is_active=True)
        context['site_slider'] = site_slider
        most_visited_products = Product.objects.filter(is_active=True, is_delete=False).annotate(
            visit_count=Count('productvisit')).order_by('-visit_count')[:12]
        context['most_visited_product'] = group_list(most_visited_products)
        categories = ProductCategory.objects.filter(is_active=True,is_delete=False)[:6]
        categories_products = []
        for category in categories:
            item = {
                'id': category.id,
                'title': category.title,
                'products': list(category.product_categories.all())[:4]
            }
            categories_products.append(item)
        context['categories_products'] = categories_products
        return context


def site_header_component(request):
    return render(request, 'shared/site-header-component.html')


def site_footer_component(request):
    return render(request, 'shared/site-footer-component.html')
