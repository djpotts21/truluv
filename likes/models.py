from django.db import models
from django.contrib.auth.models import User


class Like(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user')
    likes = models.ManyToManyField(
        User, related_name='likes')

    def __str__(self):
        return self.user.username
