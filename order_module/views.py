from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from order_module.models import Order, OrderDetail
from product_module.models import Product


# Create your views here.
def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    if count < 1:
        return JsonResponse({
            'status': 'invalid_number',
            'text': 'مقدار عدد وارد شده معتبر نمی باشد',
            'icon': 'error',
            'confirm_button_text': 'باشه ممنون'
        })
    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                new_oder = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_oder.save()

            return JsonResponse({
                'status': 'success',
                'text': 'کالای شما با موفقیت وارد سبد خرید شد',
                'icon': 'success',
                'confirm_button_text': 'باشه ممنون'
            })
        else:
            return JsonResponse({
                'status': 'no_product',
                'text': 'محصولی یافت نشد',
                'icon': 'error',
                'confirm_button_text': 'باشه ممنون'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'لطفا برای انجام عملیات خرید ابتدا وارد سایت شوید',
            'icon': 'error',
            'confirm_button_text': 'باشه ممنون'
        })
