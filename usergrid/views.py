from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from myprofile.models import Profile
from likes.views import get_user_liked_users
from likes.models import UserLike
import geopy.distance
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def usergrid(request):
    # Get current user from the request and pull profile data
    request_user_profile = Profile.objects.get(user=request.user)
    requestor_location = request_user_profile.location
    # Get the liked users of the current user
    liked_users = get_user_liked_users(request.user)
    liked_user_list = []
    for liked_user in liked_users:
        liked_user_id = liked_user.liked_user.id
        liked_user_list.append(liked_user_id)

    # Get all users from the database
    users = User.objects.all()

    # Create a dictionary to store the users and their location
    user_prof = {}
    for user in users:
        profile_data = get_object_or_404(Profile, user=user)
        if profile_data.image1:
            image1 = profile_data.image1.url
        else:
            image1 = 'https://i.ibb.co/ssFD4BX/no-image.png'
        location = profile_data.location
        id = profile_data.id
        premium_status = Profile.objects.get(user=user).premium_user_account

        distance = geopy.distance.distance(requestor_location, location).miles
        distance = round(distance, 2)

        user_prof[user] = {
            'first_name': user.first_name,
            'profileid': id,
            'image1': image1,
            'distance': distance,
        }
        user_prof_sorted = sorted(user_prof.items(),
                                  key=lambda x: x[1]['distance'])
        user_prof = dict(user_prof_sorted)   

        matched_users = []
        current_user = request.user
        likes = UserLike.objects.filter(user=current_user)
        for like in likes:
            liked_user = like.liked_user
            liked_user_likes = UserLike.objects.filter(user=liked_user)
            for liked_user_like in liked_user_likes:
                if liked_user_like.liked_user == current_user:
                    matched_users.append(liked_user.id)  

    # is current user a premium user?
    current_user = request.user
    current_user_profile = Profile.objects.get(user=current_user)
    premium_status = current_user_profile.premium_user_account


    # Create a context dictionary to pass to the template
    context = {
        'user_prof': user_prof,
        'liked_users': liked_user_list,
        'matched_users': matched_users,
        'premium_status': premium_status,
    }

    return render(request, 'usergrid/usergrid.html', context)
