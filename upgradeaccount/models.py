import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from myprofile.models import Profile


class UpgradeOrder(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField(auto_now_add=True)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_order = models.TextField(null=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Set total to UPGRADE_COST in settings.py
        """
        self.total = settings.UPGRADE_COST
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number