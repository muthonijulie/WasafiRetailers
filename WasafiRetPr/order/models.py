from django.db import models
from django.contrib.auth import get_user_model
from WasafiRet.models import Product  

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
  
   
    shipping_name = models.CharField(max_length=255)
    shipping_email = models.EmailField()
    shipping_address = models.TextField()
    shipping_city = models.CharField(max_length=100)
    shipping_zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
