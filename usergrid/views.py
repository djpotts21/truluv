from django.shortcuts import render
from django.contrib.auth.models import User
from myprofile.models import Profile


# Create your views here.

def usergrid(request):
    # Get all users from the database
    users = User.objects.all()

    # Get users location from profiles table in the database
    profiles = Profile.objects.all()

    # Create a dictionary to store the users and their location
    user_prof = {}
    for user in users:
        for profile in profiles:
            if user.id == profile.user_id:
                user_prof[user] = {
                    'location': profile.location,
                    'image_1': profile.image1.url,
                    'first_name': user.first_name,
                    'userid': user.id,
                }
                print(user_prof[user])

    # Pass user location, image1 and first name and 
    # userid to the template as context
    context = {
        'user_prof': user_prof,
    }

    return render(request, 'usergrid/usergrid.html', context)
