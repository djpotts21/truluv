from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    flaged = models.BooleanField(default=False)
    sender_name = models.CharField(max_length=100, default='')
    receiver_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.message
