from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Like
from django.http import JsonResponse
import geopy.distance


def like_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        liked_user_id = request.POST.get('liked_user_id')
        user = User.objects.get(id=user_id)
        liked_user = User.objects.get(id=liked_user_id)
        like, created = Like.objects.get_or_create(user=user)
        like.likes.add(liked_user)
        like.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


def unlike_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        liked_user_id = request.POST.get('liked_user_id')
        user = User.objects.get(id=user_id)
        liked_user = User.objects.get(id=liked_user_id)
        like = Like.objects.get(user=user)
        like.likes.remove(liked_user)
        like.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


def get_likes(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        user = User.objects.get(id=user_id)
        likes = Like.objects.filter(likes=user)
        users = []
        for like in likes:
            users.append(like.user)
        return JsonResponse({'users': users})
    return JsonResponse({'status': 'error'})


def get_who_likes_me(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        user = User.objects.get(id=user_id)
        likes = Like.objects.filter(likes=user)
        users = []
        for like in likes:
            users.append(like.user)
        return JsonResponse({'users': users})
    return JsonResponse({'status': 'error'})


def get_matches(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        user = User.objects.get(id=user_id)
        likes = Like.objects.filter(likes=user)
        matches = []
        for like in likes:
            if user in like.likes.all():
                matches.append(like.user)
        return JsonResponse({'matches': matches})
    return JsonResponse({'status': 'error'})


def calc_distance(requestor_location, location):
        distance = geopy.distance.distance(requestor_location, location).miles
        distance = round(distance, 2)
        return distance


def likes(request):
    user = request.user.id
    likes = Like.objects.filter(user=user).values_list('likes', flat=True)
    who_likes_me = Like.objects.filter(likes=user).values_list('user', flat=True)
    matches = Like.objects.filter(user=user, likes=user).values_list('user', flat=True)
    requestor_location = User.objects.get(id=user).profile.location

    matched_user_profiles = {}
    liked_user_profiles = {}
    who_likes_me_profiles = {}

    for user_id in likes:
        user_profile = User.objects.get(id=user_id).profile
        user_data = User.objects.get(id=user_id)
        distance = calc_distance(requestor_location, user_profile.location)
        liked_user_profiles[user_id] = {
            'distance': distance,
            'age': user_profile.age,
            'image1': user_profile.image1.url,
            'first_name': user_data.first_name,
        }

    for user_id in who_likes_me:
        user_profile = User.objects.get(id=user_id).profile
        user_data = User.objects.get(id=user_id)
        distance = calc_distance(requestor_location, user_profile.location)
        who_likes_me_profiles[user_id] = {
            'distance': distance,
            'age': user_profile.age,
            'image1': user_profile.image1.url,
            'first_name': user_data.first_name,
        }

    for user_id in matches:
        user_profile = User.objects.get(id=user_id).profile
        user_data = User.objects.get(id=user_id)
        distance = calc_distance(requestor_location, user_profile.location)
        matched_user_profiles[user_id] = {
            'distance': distance,
            'age': user_profile.age,
            'image1': user_profile.image1.url,
            'first_name': user_data.first_name,
        }
    return render(request,
                  'likes/likes.html',
                  {
                    'liked_user_profiles': liked_user_profiles,
                    'who_likes_me_profiles': who_likes_me_profiles,
                    'matched_user_profiles': matched_user_profiles
                   })
