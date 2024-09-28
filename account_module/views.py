from django.contrib.auth import login, logout
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View

from account_module.forms import RegisterForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from account_module.models import User
from utils.email import send_email


# Create your views here.
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_pass = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'کاربر قبلا ثبت نام کرده است')
            else:
                new_user = User(email=user_email, is_active=False, username=user_email,
                                email_active_code=get_random_string(70))
                new_user.set_password(user_pass)
                new_user.save()
                send_email('فعال سازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/activate-account.html')
                return redirect(reverse('login_page'))
        else:
            raise Http404
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login-page.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    pass_is_correct = user.check_password(user_pass)
                    if pass_is_correct:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email', 'کاربری با مشخصات فوق یافت نشد')
            else:
                login_form.add_error('email', 'کاربری با مشخصات فوق یافت نشد')

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login-page.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(70)
                user.save()
                # todo: show success message to user
                return redirect(reverse('login_page'))
            else:
                # todo : show your account was activated message to  user
                pass
        raise Http404


class ForgetPasswordView(View):
    def get(self, request):
        forget_form = ForgetPasswordForm()
        context = {
            'forget_form': forget_form
        }
        return render(request, 'account_module/forget-pass.html', context)

    def post(self, request):
        forget_form = ForgetPasswordForm(request.POST)
        if forget_form.is_valid():
            user_email = forget_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'emails/activate-account.html')
        context = {
            'forget_form': forget_form
        }
        return render(request, 'account_module/forget-pass.html', context)


class ResetPasswordView(View):
    def get(self, request, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_page'))

        reset_pass_form = ResetPasswordForm()

        context = {
            'reset_pass': reset_pass_form,
            'user':user
        }
        return render(request, 'account_module/reset-pass.html', context)

    def post(self, request, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        if reset_pass_form.is_valid():
            user: User = User.objects.filter(email_active_code__iexact=active_code).first()
            if user is None:
                reset_pass_form.add_error('email', 'کاربر وجود ندارد')
            new_user_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(new_user_pass)
            user.email_active_code = get_random_string(70)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))
        context = {
            'reset_pass': reset_pass_form
        }
        return render(request, 'account_module/reset-pass.html', context)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home_page'))
