from django.urls import path
from . import views

urlpatterns=[
    path('reviews/<int:product_id>/',views.add_review,name='add_review')
    
]