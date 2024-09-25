from django.db import models
from django.utils import timezone

class MinedData(models.Model):
    order_id = models.CharField(max_length=100,unique=True)
    system_order_id = models.CharField(max_length=100)
    order_date = models.DateTimeField(default=timezone.now)  # Default value set here
    order_total = models.FloatField()
    customer_pincode = models.CharField(max_length=10)
    extra_details = models.JSONField()
    createdAt =models.DateTimeField()
    isUsed = models.BooleanField()
    used_at=None

    def __str__(self):
        return self.order_id
