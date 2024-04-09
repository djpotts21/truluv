from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from myprofile.models import Profile
from django.contrib.auth.models import User

import os, requests
import geopy.distance
from checkuserpremium.models import check_user_premium

proxyDict = {
              "http": os.environ.get('FIXIE_URL', ''),
              "https": os.environ.get('FIXIE_URL', '')
            }

@login_required
def viewuser(request, user_id):
    # Run premium user check
    check_user_premium(request)

    # Get current user from the request and pull profile data
    request_user_profile = Profile.objects.get(user=request.user)
    requestor_location = request_user_profile.location

    user = get_object_or_404(Profile, pk=user_id)
    user_data = user.__dict__

    profile_user = get_object_or_404(User, pk=user.user_id)
    user_data['first_name'] = profile_user.username
    user_data['last_name'] = profile_user.last_name

    if user_data['location'] is None:
        user_data['location'] = '0,0'
    else:
        # Get the latitude and longitude from user_data
        location = user_data.get('location')

        # Get API Key from OS
        gmapsapikey = os.environ.get('GOOGLE_MAPS_API_KEY_GEOCODE')

        # Make a request to Google's Reverse Geocoding API
        req_url = "https://maps.googleapis.com/maps/api/geocode/json?latlng="
        url = f'{req_url}{location}&key={gmapsapikey}'
        print(url)
        response = requests.get(url, proxies=proxyDict)

        data = response.json()
        print(data)  # This is the response from the API for debugging

        # Extract the town from the response
        for component in data['results'][0]['address_components']:
            if 'postal_town' in component['types']:
                town = component['long_name']
                break
        else:
            town = None

        # Save the location to user_data as 'location_clean'
        user_data['location_clean'] = town

        # Calculate the distance between the requestor and the user
        distance = geopy.distance.distance(requestor_location, location).miles
        distance = round(distance, 2)
        user_data['distance'] = distance

    context = {
        'user': user_data,
    }
    return render(request,
                  'viewuser/viewuser.html',
                  context)
