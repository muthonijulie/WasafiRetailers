from django.urls import path
from . import views

urlpatterns = [
   
    path('category_list/',views.category_list,name='category_list'),
    path('category_create/',views.category_create,name='category_create'),
    path('category_update/<int:product_id>', views.category_update, name='category_update'),
    path('category_delete/<int:product_id>', views.category_delete, name='category_delete'),
    path('',views.product_list,name='product_list'),
    path('product_create/', views.product_create, name='product_create'),
    path('product_delete/<int:product_id>', views.product_delete, name='product_delete'),
    path('product_update/<int:product_id>', views.product_update, name='product_update'),
    path('search/', views.search, name='search'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('cart/update/<int:cart_item_id>',views.update_cart,name='update_cart'),
    path('cart/remove/<int:cart_item_id>',views.remove_cart,name='remove_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail/<int:product_id>/', views.detail, name='detail'),
    

]

