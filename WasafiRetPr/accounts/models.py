from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/images', null=True, blank=True)
   
    recent_activities = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
