from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'email',
                    'phone'
                    )
    search_fields = ['user', 'email', 'phone']
    list_filter = ['created_at', 'updated_at']
    ordering = ['user']

admin.site.register(Profile, ProfileAdmin)
