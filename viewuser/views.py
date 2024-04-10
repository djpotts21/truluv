from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from myprofile.models import Profile
from likes.models import UserLike
from django.contrib.auth.models import User

import os
import requests
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

    liked_users_list = []
    liked_by_user_list = []
    matched_users_list = []

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
        response = requests.get(url, proxies=proxyDict)

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

        # Calculate the distance between the requestor and the user
        distance = geopy.distance.distance(requestor_location, location).miles
        distance = round(distance, 2)
        user_data['distance'] = distance

        # Get list of liked users id from the requestor, from the likes table
        liked_users = UserLike.objects.filter(user=request.user)
        liked_users = liked_users.values_list('liked_user', flat=True)
        for liked_user in liked_users:
            liked_users_list.append(liked_user)

        # Who has liked the requestor
        liked_by_user = UserLike.objects.filter(liked_user=request.user)
        liked_by_user = liked_by_user.values_list('user', flat=True)
        for liked_user in liked_by_user:
            liked_by_user_list.append(liked_user)

        # Create Match List
        matched_users = UserLike.objects.filter(user=request.user, liked_user=user.user_id) 
        for match in matched_users:
            matched_users_list.append(match)

        # Is user premium>
        premium_status = request_user_profile.premium_user_account

    context = {
        'user': user_data,
        'liked_users': liked_users_list,
        'matched_users': matched_users_list,
        'premium_status': premium_status
    }
    return render(request,
                  'viewuser/viewuser.html',
                  context)
