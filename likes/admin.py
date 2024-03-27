from django.contrib import admin
from .models import Like, UserswhoLikeMe, LikedUsers

admin.site.register(Like)
admin.site.register(LikedUsers)
admin.site.register(UserswhoLikeMe)

