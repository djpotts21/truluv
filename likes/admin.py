from django.contrib import admin
from .models import UserLike


# register Like to admin, but only read-only
class LikeAdmin(admin.ModelAdmin):
    verbose_name_plural = 'User Likes'
    display = 'User Likes', 'liked_user'
    search_fields = ('user__username', 'liked_user')
    list_display = ('user', 'liked_user')



admin.site.register(UserLike, LikeAdmin)