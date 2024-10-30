from django.urls import path
from WasafiRet import views
from . import views

urlpatterns=[
    
    path('flashsale/',views.flashsale,name='flashsale'),
]
