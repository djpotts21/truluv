from django.shortcuts import render, get_object_or_404
from myprofile.models import Profile
from django.contrib.auth.models import User
import os
import requests


def viewuser(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)
    user_data = user.__dict__

    profile_user = get_object_or_404(User, pk=user.user_id)
    user_data['first_name'] = profile_user.username
    user_data['last_name'] = profile_user.last_name

    # Get the latitude and longitude from user_data
    location = user_data.get('location')

    # Get API Key from OS
    gmapsapikey = os.environ.get('GOOGLE_MAPS_API_KEY_GEOCODE')

    # Make a request to Google's Reverse Geocoding API
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={location}&key={gmapsapikey}'
    response = requests.get(url)
    data = response.json()
    # Extract the town from the response
    for component in data['results'][0]['address_components']:
        if 'postal_town' in component['types']:
            town = component['long_name']
            break
    else:
        town = None

    # Save the location to user_data as 'location_clean'
    user_data['location_clean'] = town

    context = {
        'user': user_data,
    }
    print(user_data)
    return render(request,
                  'viewuser/viewuser.html',
                  context)
