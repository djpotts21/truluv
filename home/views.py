from django.shortcuts import render
from checkuserpremium.models import check_user_premium


def home(request):
    # Run premium user check
    check_user_premium(request)

    return render(request, 'home/home.html', {})
