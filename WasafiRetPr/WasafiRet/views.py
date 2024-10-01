from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Category,Cart,CartItem
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
def search(request):
     search_query=request.GET.get('search','')
     if search_query:
        product=Product.objects.filter(name__icontains=search_query)
     else:
          product=Product.objects.none()
     return render(request,'WasafiRet/product.html',{'search_query':search_query,'product':product})
    
def view_cart(request):
    cart=Cart.objects.filter(user=request.user).first()
    cart_items=CartItem.objects.filter(cart=cart)

    cart_total=sum(item.get_total() for item in cart_items)
    return render(request, 'WasafiRet/cart.html', {'cart_items':cart_items, 'cart_total':cart_total})

def add_to_cart(request,product_id):
     product=Product.objects.get(id=product_id)
     cart,created=Cart.objects.get_or_create(user=request.user)
     cart_item,created=CartItem.objects.get_or_create(cart=cart,product=product)

     if not created:
          cart_item.quantity+=1
     else:
          cart_item.quantity=1

     cart_item.save()
     return redirect('view_cart')

def checkout(request):
    return render(request, 'WasafiRet/checkout.html')


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'WasafiRet/product_detail.html', {'product': product})
