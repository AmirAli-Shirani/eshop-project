from django.urls import path

from . import views

urlpatterns = [
    # path('', views.contact_us_page),
    path('', views.ContactUsFormView.as_view(),name='contact_us_page'),
    path('create-profile-page', views.CreateProfileView.as_view(),name='create_profile_page'),
    path('profile-page', views.ProfilePage.as_view(),name='profile_page'),
]
