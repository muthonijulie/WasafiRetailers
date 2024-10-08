from django.contrib import admin
from .models import Flashsale

# Register your models here.

admin.site.register(Flashsale)

class Flashsaleadmin(admin.ModelAdmin):
    list=['name','product','image','discount','start_time','end_time']