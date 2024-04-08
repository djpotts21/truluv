from django.db import models
import uuid


class UpgradeOrder(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField(auto_now_add=True)
    order_number = models.UUIDField(default=uuid.uuid4, editable=False)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, default='')

    def __str__(self):
        return self.full_name
