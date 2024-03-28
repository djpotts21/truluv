from django.contrib import admin
from .models import Like


# register Like to admin, but only read-only
class LikeAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'likes')
    verbose_name_plural = 'User Likes'
    display = 'User Likes'
    search_fields = ('user__username', 'likes__username')


admin.site.register(Like, LikeAdmin)