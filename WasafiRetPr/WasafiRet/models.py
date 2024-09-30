from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def _str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to=',media/images',blank=True,null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart {self.id} for {self.user.username}'
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} in Cart {self.cart.id}'
    
    def get_total(self):
        return self.quantity*self.product.price