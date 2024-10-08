from django.db import models
from django.utils import timezone
from WasafiRet.models import Product


# Create your models here

class Flashsale(models.Model):
    name=models.CharField(max_length=255)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media/images',blank=True,null=True)
    discount=models.DecimalField(max_digits=10,decimal_places=2)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    def is_active(self):
        return self.start_time<=timezone.now()<=self.end_time
