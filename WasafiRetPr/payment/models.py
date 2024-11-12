from django.db import models

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    checkout_id = models.CharField(max_length=50, unique=True)
    mpesa_code = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mpesa_code} - {self.amount} KES"
