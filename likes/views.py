from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserLike
from myprofile.models import Profile
import geopy.distance

# Add user to likes
def add_like(request, user_id):
    # check if user is already liked
    if UserLike.objects.filter(user=request.user, liked_user=User.objects.get(id=user_id)).exists():
        return redirect('view_likes')
    else:
        liked_user = User.objects.get(id=user_id)
        user = request.user
        UserLike.objects.create(user=user, liked_user=liked_user)
        return redirect('view_likes')


# Remove user from likes
def remove_like(request, object_id):
    liked_user = UserLike.objects.get(id=object_id)
    liked_user.delete()
    return redirect('view_likes')


# Get requesters user liked users
def get_user_liked_users(user):
    liked_users = UserLike.objects.filter(user=user)
    return liked_users


# Get who likes the requested user
def get_user_liked_by_users(user):
    liked_by_users = UserLike.objects.filter(liked_user=user)
    return liked_by_users


# render the template with the liked users and the liked by users with the distance, age from user profile and user first name
def view_likes(request):
    user = request.user
    liked_users = get_user_liked_users(user)
    liked_by_users = get_user_liked_by_users(user)
    profile = Profile.objects.get(user=user)
    user_location = (profile.location)
    liked_users_list = []
    for liked_user in liked_users:
        liked_user_profile = Profile.objects.get(user=liked_user.liked_user)
        liked_user_location = (liked_user_profile.location)
        distance = geopy.distance.distance(user_location, liked_user_location).km
        liked_user.distance = distance
        liked_user.age = liked_user_profile.age
        liked_user.first_name = liked_user_profile.user.first_name
        liked_user_dict = {
            'object_id': liked_user.id,
            'user_id': liked_user.user.id,
            'distance': distance,
            'age': liked_user_profile.age,
            'name': liked_user_profile.user.first_name,
            'image1': liked_user_profile.image1.url if liked_user_profile.image1 else 'https://i.ibb.co/ssFD4BX/no-image.png'
        }
        liked_users_list.append(liked_user_dict)

    for liked_by_user in liked_by_users:
        liked_by_user_profile = Profile.objects.get(user=liked_by_user.user)
        liked_by_user_location = (liked_by_user_profile.location)
        distance = geopy.distance.distance(user_location, liked_by_user_location).km
        liked_by_user.distance = distance
        liked_by_user.age = liked_by_user_profile.age
        liked_by_user.first_name = liked_by_user_profile.user.first_name
    return render(request, 'likes/likes.html', {'liked_users': liked_users_list, 'liked_by_users': liked_by_users})
