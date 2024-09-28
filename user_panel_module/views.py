from django.contrib.auth import logout
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from account_module.models import User
from order_module.models import Order, OrderDetail
from user_panel_module.forms import EditProfileModelForm, ChangePasswordForm


# Create your views here.
class UserPanelDashboard(TemplateView):
    template_name = 'user_panel_module/dashboard.html'


class EditProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_profile = EditProfileModelForm(instance=current_user)
        context = {
            'form': edit_profile,
            'current_user': current_user
        }
        return render(request, 'user_panel_module/edit-user-profile.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_profile = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_profile.is_valid():
            edit_profile.save(commit=True)
        context = {
            'form': edit_profile,
            'current_user': current_user
        }
        return render(request, 'user_panel_module/edit-user-profile.html', context)


def user_panel_menu_components(request):
    return render(request, 'user_panel_module/components/profile-edit-page.html')


class ChangePasswordView(View):
    def get(self, request: HttpRequest):
        form = ChangePasswordForm()
        context = {
            'form': form
        }
        return render(request, 'user_panel_module/change-password.html', context)

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('password', 'کلمه عبور وارد شده اشتباه است')
        context = {
            'form': form
        }
        return render(request, 'user_panel_module/change-password.html', context)


def user_basket(request: HttpRequest):
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total_price()
    context = {
        'order': current_order,
        'sum': total_amount
    }
    return render(request, 'user_panel_module/cart.html', context)


def remove_order_detail(request: HttpRequest):
    detail_id = request.GET.get('detailId')
    if detail_id is not None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })
    deleted_count, deleted_dict = OrderDetail.objects.filter(id=detail_id, order__is_paid=False,
                                                             order__user_id=request.user.id).delete()
    if deleted_count == 0:
        return JsonResponse({
            'status': 'detail_not_found'
        })
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()
    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user-basket-content.html', context)
    })
