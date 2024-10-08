from django.urls import path
from .import views

urlspattern=[
    path('flashsale/',views.flashsale, name='flashsale')
]