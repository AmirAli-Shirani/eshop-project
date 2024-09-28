from . import views
from django.urls import path

urlpatterns=[
    path('',views.ArticleListView.as_view(),name='article_page'),
    path('cat/<str:category>',views.ArticleListView.as_view(),name='article_by_category_page'),
    path('<pk>',views.ArticleDetailView.as_view(),name='article_detail_page')
]