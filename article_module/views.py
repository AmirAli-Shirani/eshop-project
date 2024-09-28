from django.shortcuts import render
from django.views.generic import ListView, DetailView

from article_module.models import Articles, ArticleCategory
from site_module.models import SiteBanner


# Create your views here.
class ArticleListView(ListView):
    model = Articles
    paginate_by = 1
    template_name = 'article_module/article.html'
    context_object_name = 'articles'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['banners']=SiteBanner.objects.filter(is_active=True,position__iexact=SiteBanner.SiteBannerChoices.article_page)
        return context

    def get_queryset(self):
        query = super(ArticleListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query


def article_category_component(request):
    article_main_categories = ArticleCategory.objects.prefetch_related('articlecategory_set').filter(is_active=True, parent_id=None)
    context = {
        'main_categories': article_main_categories
    }
    return render(request, 'article_module/components/article-categories-components.html', context)


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'article_module/article-detail.html'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query
