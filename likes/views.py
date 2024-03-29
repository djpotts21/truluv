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
    liked_users = []  # Initialize liked_users as an empty list
    for like in likes:
        liked_user = like.id
        profile = Profile.objects.get(user=liked_user)
        userdata = User.objects.get(id=liked_user)
        name = userdata.first_name
        if profile.image1:
            image1 = profile.image1.url
        else:
            image1 = 'https://i.ibb.co/ssFD4BX/no-image.png'
        distance = geopy.distance.distance(user.profile.location, profile.location)
        distance = round(distance.miles, 2)
        age = profile.age
        liked_users.append({  # Use append() method to add liked user details to the list
            'name': name,
            'distance': distance,
            'age': age,
            'image1': image1,
            'liked_user_id': liked_user
        })
    
    wholikesme = Like.objects.filter(likes=user)
    who_likes_me = []
    print(wholikesme)
    for like in wholikesme:
        print(like)
        liked_user = like.user
        profile = Profile.objects.get(user=liked_user)
        userdata = User.objects.get(id=liked_user.id)
        name = userdata.first_name
        if profile.image1:
            image1 = profile.image1.url
        else:
            image1 = 'https://i.ibb.co/ssFD4BX/no-image.png'
        distance = geopy.distance.distance(user.profile.location, profile.location)
        distance = round(distance.miles, 2)
        age = profile.age
        who_likes_me.append({  # Use append() method to add liked user details to the list
            'name': name,
            'distance': distance,
            'age': age,
            'image1': image1,
            'liked_user_id': liked_user.id
        })

    return render(request,
                  'likes/likes.html',
                  context={
                      'likes': liked_users,
                      'wholikesme': who_likes_me
                      })
