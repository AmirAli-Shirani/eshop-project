from django.shortcuts import render


# Create your views here.

def index_page(request):
    return render(request, 'home_module/index.html')


def header_component(request):
    return render(request, 'shared/header-component.html')


def footer_component(request):
    return render(request, 'shared/footer-component.html')
