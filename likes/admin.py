from django.contrib import admin
from .models import Like


# register Like to admin, but only read-only
class LikeAdmin(admin.ModelAdmin):
    verbose_name_plural = 'User Likes'
    display = 'User Likes'
    search_fields = ('user__username', 'likes__username')


admin.site.register(Like, LikeAdmin)