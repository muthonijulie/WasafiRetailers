from django.urls import path
from . import views

app_name = "payment"

urlpatterns = [
    path("", views.payment_view, name="payment"),
    path('initiate-stk-push/', views.initiate_stk_push, name='initiate-stk-push'),

   
]

