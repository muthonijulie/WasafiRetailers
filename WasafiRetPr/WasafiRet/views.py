from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Category
from .forms import ProductCreateForm,CategoryForm

# Create your views here.
def Home(request):
       return render(request, 'WasafiRet/home.html',)

def category_list(request):
     categories=Category.objects.all()
     return render(request,'WasafiRet/category_list.html',{'categories':categories}) 

def category_create(request):
      if request.method == 'POST':
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
      else:
            form=CategoryForm()
          
      return render(request,'WasafiRet/category_form.html',{'form':form})
def product_list(request):
    products=Product.objects.all()

    return render(request, 'WasafiRet/product.html',{'products':products})

def product_create(request):
    if request.method == 'POST':
        form=ProductCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
            form=ProductCreateForm()
          


    return render(request, 'WasafiRet/product_create.html',{'form':form})

def cart(request):
    return render(request, 'WasafiRet/cart.html')

def checkout(request):
    return render(request, 'WasafiRet/checkout.html')


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'WasafiRet/product_detail.html', {'product': product})
