from django.urls import path
from . import views

urlpatterns = [
   
    path('category_list/',views.category_list,name='category_list'),
    path('category_create/',views.category_create,name='category_create'),
    path('',views.product_list,name='product_list'),
    path('product_create/', views.product_create, name='product_create'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail/<int:product_id>/', views.detail, name='detail'),

]
