from django.urls import path

from home_module import views

urlpatterns = [
    path('', views.index_page, name='home_page')
]
