from django.db import models
from django.contrib.auth.models import User


# Store each like of a user with the logged in user and the liked user
class UserLike(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='requesting_user')
    liked_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='liked_user')

    def __str__(self):
        return self.user.username
