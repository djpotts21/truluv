from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from myprofile.models import Profile
import geopy.distance


# Create your views here.

def usergrid(request):
    # Get current user from the request and pull profile data
    request_user_profile = Profile.objects.get(user=request.user)
    requestor_location = request_user_profile.location


    # Get all users from the database
    users = User.objects.all()
        # Create a dictionary to store the users and their location
    user_prof = {}
    for user in users:
        profile_data = get_object_or_404(Profile, user=user)

        image1 = profile_data.image1.url
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
        print(user_prof)

    # Pass user location, image1 and first name and 
    # userid to the template as context
    context = {
        'user_prof': user_prof,
    }

    return render(request, 'usergrid/usergrid.html', context)
