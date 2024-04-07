from django.contrib import admin
from .models import UpgradeOrder


class UpgradeOrderAdmin(admin.ModelAdmin):
    list_display = ('full_name',
                    'email',
                    'phone_number',
                    'date',
                    'order_number',
                    'total',
                    'stripe_pid'
                    )
    search_fields = ['full_name', 'email', 'phone_number']
    list_filter = ['date']
    ordering = ['date']

admin.site.register(UpgradeOrder, UpgradeOrderAdmin)
