from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Like
import geopy.distance


def like_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        liked_user_id = request.POST.get('liked_user_id')
        user = User.objects.get(id=user_id)
        liked_user = User.objects.get(id=liked_user_id)
        like = Like(user=user, likes=liked_user)
        like.save()
    return render(request, 'likes/likes.html')


def unlike_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        liked_user_id = request.POST.get('liked_user_id')
        user = User.objects.get(id=user_id)
        liked_user = User.objects.get(id=liked_user_id)
        like = Like.objects.get(user=user, likes=liked_user)
        like.delete()
    return render(request, 'likes/likes.html')


def view_likes(request):
    user_id = 1
    user = User.objects.get(id=user_id)
    likes = Like.objects.filter(user=user)
    wholikesme = Like.objects.filter(likes=user)
    return render(request,
                  'likes/likes.html',
                  {'likes': likes},
                  {'wholikesme': wholikesme})