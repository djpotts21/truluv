from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender',
                    'receiver',
                    'message',
                    'timestamp',
                    'read',
                    'read_at',
                    'flagged'
                    )
    search_fields = ['sender', 'receiver', 'message']
    list_filter = ['timestamp', 'read', 'read_at', 'flagged']
    ordering = ['timestamp']


admin.site.register(Message, MessageAdmin)
