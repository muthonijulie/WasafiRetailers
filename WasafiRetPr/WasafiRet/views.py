from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Category,Cart,CartItem
from .forms import ProductCreateForm,CategoryForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponseBadRequest
from django.db.models import Q
from flashsale.models import Flashsale
from django.utils import timezone
from review.models import Review
# Create your view here.
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
    paginator=Paginator(products,10,orphans=10,allow_empty_first_page=True)
    page=request.GET.get('page')
    try:
         paginated_products=paginator.page(page)
    except PageNotAnInteger:
         paginated_products=paginator.page(1)
    except EmptyPage:
         paginated_products=paginator.page(paginator.num_pages)

         
    return render(request, 'WasafiRet/product.html',{'products':paginated_products})

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
     search_query=request.POST.get('search_query','')
    
     products=Product.objects.filter(Q(name__icontains=search_query))
     context={
          'products':products,
          'search_query':search_query,
     }
     return render(request,'WasafiRet/search.html',context)
    
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
def update_cart(request,cart_item_id):
     cart_item=get_object_or_404(CartItem,id=cart_item_id)
     
     if request.method =='POST':
          new=int(request.POST.get('quantity',0))
          if new>0:
               cart_item.quantity=new
               cart_item.save()
          else:
               return HttpResponseBadRequest("Invalid quantity")
          return redirect('view_cart')
     return HttpResponseBadRequest("Invalid request method")
def remove_cart(request,cart_item_id):
  
     cart_item=get_object_or_404(CartItem,id=cart_item_id)

     
     if request.method in ['POST','GET']:
        cart_item.delete()
     
        return redirect('view_cart')
     return HttpResponseBadRequest("Invalid request method")
    

def checkout(request):
    return render(request, 'WasafiRet/checkout.html')


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews=product.reviews.all()
    return render(request, 'WasafiRet/product_detail.html', {'product': product,'reviews':reviews})

def main(request):
     current=timezone.now()
     flashsale=Flashsale.objects.filter(start_time__lte=current,end_time__gte=current)
     return render(request, 'WasafiRet/product.html',{'flashsale':flashsale})
     
