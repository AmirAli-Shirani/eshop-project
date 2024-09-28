from django.shortcuts import render
from django.views.generic import ListView

from article_module.models import Article


# Create your views here.

class ArticleListView(ListView):
    template_name = 'article_module/article-list.html'
    paginate_by = 3
    model = Article
    context_object_name = 'articles'
