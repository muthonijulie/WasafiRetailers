from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'WasafiRet/home.html')

def product(request):
    return render(request, 'WasafiRet/product.html')

def cart(request):
    return render(request, 'WasafiRet/cart.html')

def checkout(request):
    return render(request, 'WasafiRet/checkout.html')

def detail(request):
    return render(request, 'WasafiRet/product_detail.html')
