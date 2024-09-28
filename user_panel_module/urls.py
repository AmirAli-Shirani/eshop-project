from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboard.as_view(), name='user_panel_page'),
    path('edit-profile', views.EditProfilePage.as_view(), name='user_edit_profile_page'),
    path('change_pass', views.ChangePasswordView.as_view(), name='user_change_pass_page'),
    path('cart', views.user_basket, name='user_basket_page'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail_ajax'),
]
