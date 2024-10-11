from django.contrib import admin
from .models import Flashsale

# Register your models here.
class FlashsaleAdmin(admin.ModelAdmin):
    list=('name','price','discount','start_time','end_time','image')

admin.site.register(Flashsale,FlashsaleAdmin)