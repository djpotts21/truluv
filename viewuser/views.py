from django.shortcuts import render, get_object_or_404
from myprofile.models import Profile
from django.contrib.auth.models import User


def viewuser(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)
    user_data = user.__dict__

    profile_user = get_object_or_404(User, pk=user.user_id)
    user_data['first_name'] = profile_user.username
    user_data['last_name'] = profile_user.last_name

    context = {
        'user': user_data,
    }
    print(user_data)
    return render(request,
                  'viewuser/viewuser.html',
                  context)
