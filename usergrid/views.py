from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from myprofile.models import Profile


# Create your views here.

def usergrid(request):
    # Get all users from the database
    users = User.objects.all()

    # Create a dictionary to store the users and their location
    user_prof = {}
    for user in users:
        profile_data = get_object_or_404(Profile, user=user)

        image1 = profile_data.image1.url
        location = profile_data.location
        
        user_prof[user] = {
            'first_name': user.first_name,
            'userid': user.id,
            'image1': image1,
            'location': location,
        }
        print(user_prof)

    # Pass user location, image1 and first name and 
    # userid to the template as context
    context = {
        'user_prof': user_prof,
    }

    return render(request, 'usergrid/usergrid.html', context)
