from django.shortcuts import render
from django.utils import timezone
from .models import Flashsale

# Create your views here.
def flashsale(request):
    current=timezone.now()
    flashsales=Flashsale.object.filter(start_time__lte=current,end_time__gte=current)
    return render(request,'flashsale/flash.html',{'flashsales':flashsales})

