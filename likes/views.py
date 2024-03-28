from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Like
from myprofile.models import Profile
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
    user = request.user
    likes = Like.objects.get(user=user).likes.all()
    liked_users = {}
    for like in likes:
        liked_user = like.id
        profile = Profile.objects.get(user=liked_user)
        userdata = User.objects.get(id=liked_user)
        name = userdata.first_name
        if profile.image1:
            image1 = profile.image1
        else:
            image1 = 'https://i.ibb.co/ssFD4BX/no-image.png'
        distance = geopy.distance.distance(user.profile.location, profile.location)
        age = profile.age
        liked_users = ({
            'name': name,
            'distance': distance,
            'age': age,
            'image1': image1
        })
    
    print(likes.all())
    wholikesme = Like.objects.filter(likes=user)
    return render(request,
                  'likes/likes.html', 
                  context = {
                      'likes': liked_users,
                      'wholikesme': wholikesme
                      })