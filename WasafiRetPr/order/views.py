from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import OrderForm
from WasafiRet.models import Cart, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartItem.objects.filter(cart=cart)
    cart_total = sum(item.get_total() for item in cart_items)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
           
            order = form.save(commit=False)  
            order.user = request.user  
            order.status = 'Pending'  
            order.save()  

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )

            
            cart_items.delete()

            return redirect('orders:order_confirmation', order_id=order.id)
    else:
        form = OrderForm()

    return render(request, 'order/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'cart_total': cart_total,
    })

@login_required
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    order_total = order.get_order_total()  
    return render(request, 'order/order_confirmation.html', {
        'order': order,
        'order_total': order_total, 
    })

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order/order_history.html', {'orders': orders})