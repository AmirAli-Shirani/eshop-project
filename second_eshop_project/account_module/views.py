from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views.generic import View, CreateView
import sweetify
from account_module.forms import RegisterForm, LoginForm
from account_module.models import User
from services.send_email import send_email


# Create your views here.
class RegisterView(View):
    def get(self, request: HttpRequest):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            first_name = register_form.cleaned_data.get('first_name')
            last_name = register_form.cleaned_data.get('last_name')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'کاربری با این ایمیل از قبل وجود دارد')
            else:
                new_user = User(first_name=first_name, last_name=last_name, email=user_email, is_active=False,
                                email_active_code=get_random_string(72), username=f'{first_name} {last_name}')
                new_user.set_password(user_password)
                new_user.save()
                # todo : send email to user for active its account
                send_email('بازیابی حساب کاربری', [new_user.email], {'user': new_user}, 'emails/activate-account.html')
                sweetify.info(self.request, 'موفقیت آمیز', button='اوکی',
                              text='شما با موفقیت در سایت ثبت نام شدید اما برای اطمینان از صحیح بودن ایمیل شما باید حساب کاربری شما فعال شود. از طریق لینکی که برای شما ارسال کردیم حساب کاربری خود را فعال کنید',
                              persistent=True)
                return redirect(reverse('login_page'))
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)


class LoginView(View):
    def get(self, request: HttpRequest):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=email).first()
            if user is not None:
                if user.is_active:
                    user_check_pass = user.check_password(password)
                    if user_check_pass:
                        login(request, user)
                        sweetify.success(request, 'موفقیت آمیز', persistent=True,
                                         text='شما با موفقیت وارد حساب کاربری خود شدید')
                        return redirect('/')
                    else:
                        login_form.add_error('email', 'مشخصات حساب کاربری درست نمی باشد')
                else:
                    login_form.add_error('email', 'حساب کاربری شما فعال نیست')
            else:
                login_form.add_error('email', 'کاربری با مشخصات فوق یافت نشد')
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.get(email_active_code__iexact=email_active_code)
        if user is not None:
            user.is_active = True
            user.email_active_code = get_random_string(72)
            user.save()
            sweetify.success(request, 'موفقیت آمیز', persistent=True, text='حساب کاربری شما با موفقیت فعال شد')
            return redirect('/')
        else:
            sweetify.error(request, 'شکست', persistent=True, text='کاربری با مشخصات فوق یافت نشد')
            return redirect(reverse('login_page'))


class ForgetPasswordView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
