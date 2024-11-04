from django.db import models

# Create your models here.
class Flashsale(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    discount=models.DecimalField(max_digits=5,decimal_places=2)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    image=models.ImageField(upload_to=',media/images',blank=True,null=True)

    def __str__(self):
        return self.name
