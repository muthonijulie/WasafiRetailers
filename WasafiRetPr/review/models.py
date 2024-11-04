from django.db import models
from django.contrib.auth.models import User
from WasafiRet.models import Product

# Create your models here.
class Review(models.Model):
    product=models.ForeignKey(Product,related_name='reviews',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    rating=models.IntegerField(choices=[(i,i) for i in range(1,6)])
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user}-{self.product} (Rating:{self.rating})"