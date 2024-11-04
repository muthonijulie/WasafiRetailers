from django.urls import path
from . import views

urlpatterns = [

    path('payment/initiate-stk-push/', views.initiate_stk_push, name='initiate-stk-push'),

    # Add your URL patterns here
]

