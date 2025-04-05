

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class PaymentInformation(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('card', 'Credit/Debit Card'),
        ('paypal', 'PayPal'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, blank=True)
    expiration_date = models.CharField(max_length=5, blank=True)  # MM/YY
    cvv = models.CharField(max_length=4, blank=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    save_for_future = models.BooleanField(default=False)
    subscription_active = models.BooleanField(default=False)
    subscription_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s payment info"                  