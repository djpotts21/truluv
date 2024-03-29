from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from myprofile.models import Profile
from likes.views import get_user_liked_users
import geopy.distance


# Create your views here.

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

    # Create a context dictionary to pass to the template
    context = {
        'user_prof': user_prof,
        'liked_users': liked_user_list,
    }

    return render(request, 'usergrid/usergrid.html', context)
