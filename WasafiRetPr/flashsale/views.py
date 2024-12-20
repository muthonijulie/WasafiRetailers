from django.shortcuts import render
from django.utils import timezone
from .models import Flashsale


# Create your views here.
def flashsale(request):
    current=timezone.now()
    
    flashsale=Flashsale.objects.filter(start_time__lte=current,end_time__gte=current)
   
    return render(request, 'flashsale/flash.html', {'flashsale':flashsale})