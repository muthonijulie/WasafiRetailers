from django.shortcuts import render,get_object_or_404,redirect
from .forms import ReviewForm
from WasafiRet.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_review(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.product=product
            review.user=request.user
            review.save()
            return redirect('detail',product_id=product_id)
    else:
        form=ReviewForm()
    return render(request,'review/review.html', {'form':form,'product':product})