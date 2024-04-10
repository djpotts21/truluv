from myprofile.models import Profile
from datetime import date
from django.contrib import messages


def check_user_premium(request):
    # Check if user logged in
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        profile_expiry = profile.premium_expiry
        profile_premium = profile.premium_user_account
        if profile_premium is True:
            # Check expiry date and update if expired
            if profile_expiry is not None:
                if profile.premium_expiry < date.today():
                    profile.premium_user_account = False
                    messages.error(request, 'Your premium account has expired')
                    profile.save()
            else:
                profile.premium_user_account = False
                profile.save()

        else:
            if profile_expiry is not None:
                if profile.premium_expiry > date.today():
                    messages.success(request, 'You are a premium user. Welcome back!')
                    profile.premium_user_account = True
                    profile.save()
