from django.db import models
from django.utils import timezone


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

class Flashsale(models.Model):
    name=models.CharField(max_length=255)
    product=models.ForeignKey('Product',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media/images',blank=True,null=True)
    discount=models.DecimalField(max_digits=10,decimal_places=2)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()


    def __str__(self):
        return self.name
    def is_active(self):
        return self.start_time<=timezone.now()<=self.end_time
