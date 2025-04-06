

# Register your models here.

from django.contrib import admin
from .models import PaymentInformation

@admin.register(PaymentInformation)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_method', 'subscription_active', 'subscription_date')
