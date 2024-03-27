from django.db import models
from django.contrib.auth.models import User


class LikedUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class UserswhoLikeMe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField('LikedUsers',
                                   related_name='likes',
                                   blank=True)
    wholikesme = models.ManyToManyField('UserswhoLikeMe',
                                        related_name='wholikesme',
                                        blank=True)

    def __str__(self):
        return self.user.username
