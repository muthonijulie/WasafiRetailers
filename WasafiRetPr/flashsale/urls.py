from django.urls import path
from .import views

urlpatterns=[
    path('flashsale/',views.flashsale, name='flashsale')
]