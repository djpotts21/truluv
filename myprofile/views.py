from django.shortcuts import render, redirect
import os
from . models import Profile
from django.contrib.auth.decorators import login_required
from checkuserpremium.models import check_user_premium
from django.contrib import messages
from chat.views import check_unread_messages 




@login_required
def myprofile(request):
    # Check for unread messages
    check_unread_messages(request)
    # check if user has a profile created in profile table. if not create one
    if not hasattr(request.user, 'profile'):
        profile = Profile(user=request.user)
        profile.save()

    # Run premium user check
    check_user_premium(request)

    # Google API Key for Maps on Profile
    gmapsapikey = os.environ.get('GOOGLE_MAPS_API_KEY')

    if request.user.is_authenticated:
        messages.add_message(
            request,
            messages.INFO,
            'Welcome to your profile! Please fill out your profile\
                  information to get started.')
        return render(request, 'myprofile/myprofile.html', {
            'gmapsapikey': gmapsapikey
        })    
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You must be logged in to view this page.')
        return redirect('account_login')



@login_required
def updatename(request):
    if request.POST:
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        messages.add_message(
            request,
            messages.INFO,
            'Name Updated!')
        return redirect('myprofile')


@login_required
def updateusername(request):
    if request.POST:
        user = request.user
        print(request.POST['username'])
        user.username = request.POST['username']
        user.save()
        messages.add_message(
            request,
            messages.INFO,
            'Username Updated!')
        return redirect('myprofile')


@login_required
def updateaddress(request):
    if request.POST:
        user = request.user
        user.profile.address = request.POST['address']
        user.profile.save()
        messages.add_message(
            request,
            messages.INFO,
            'Address Updated!')
        return redirect('myprofile')


@login_required
def updatephone(request):
    if request.POST:
        user = request.user
        user.profile.phone = request.POST['phone']
        user.profile.save()
        messages.add_message(
            request,
            messages.INFO,
            'Phone Number Updated!')
        return redirect('myprofile')


@login_required
def updateage(request):
    if request.POST:
        user = request.user
        user.profile.age = request.POST['age']
        user.profile.save()
        messages.add_message(
            request,
            messages.INFO,
            'Age Updated!')
        return redirect('myprofile')


@login_required
def uploadphotos(request):
    if request.POST:
        user = request.user
        if 'image1' in request.FILES:
            user.profile.image1 = request.FILES['image1']
        if 'image2' in request.FILES:
            user.profile.image2 = request.FILES['image2']
        if 'image3' in request.FILES:
            user.profile.image3 = request.FILES['image3']
        if 'image4' in request.FILES:
            user.profile.image4 = request.FILES['image4']
        if 'image5' in request.FILES:
            user.profile.image5 = request.FILES['image5']
        if 'image6' in request.FILES:
            user.profile.image6 = request.FILES['image6']
        if 'image7' in request.FILES:
            user.profile.image7 = request.FILES['image7']
        user.profile.save()
        messages.add_message(
            request,
            messages.INFO,
            'Photos Updated!')
        return redirect('myprofile')


@login_required
def removeimage(request):
    image_id = int(request.GET.get('image_id'))
    print(image_id)
    user = request.user
    if image_id == 1:
        user.profile.image1.delete()

    if image_id == 2:
        user.profile.image2.delete()

    if image_id == 3:
        user.profile.image3.delete()

    if image_id == 4:
        user.profile.image4.delete()

    if image_id == 5:
        user.profile.image5.delete()

    if image_id == 6:
        user.profile.image6.delete()

    if image_id == 7:
        user.profile.image7.delete()

    user.profile.save()
    messages.add_message(
        request,
        messages.INFO,
        'Image Deleted!')
    return redirect('myprofile')


@login_required
def updatelocation(request):
    if request.POST:
        user = request.user
        user.profile.location = request.POST['location']
        user.profile.save()
        messages.add_message(
            request,
            messages.INFO,
            'Location Updated!')
        return redirect('myprofile')


@login_required
def resetlocation(request):
    user = request.user
    user.profile.location = None
    user.profile.save()
    messages.add_message(
        request,
        messages.INFO,
        'Location Reset!')
    return redirect('myprofile')


@login_required
def updatebio(request):
    if request.POST:
        user = request.user
        user.profile.bio = request.POST['bio']
        user.profile.save()
        messages.add_message(
            request,
            messages.INFO,
            'Bio Updated!')
        return redirect('myprofile')


@login_required
def updatesocials(request):
    if request.POST:
        user = request.user
        if 'facebook' in request.POST:
            user.profile.facebook = request.POST['facebook']
        if 'twitter' in request.POST:
            user.profile.twitter = request.POST['twitter']
        if 'instagram' in request.POST:
            user.profile.instagram = request.POST['instagram']
        if 'onlyfans' in request.POST:
            user.profile.onlyfans = request.POST['onlyfans']
        if 'snapchat' in request.POST:
            user.profile.snapchat = request.POST['snapchat']
        if 'tiktok' in request.POST:
            user.profile.tiktok = request.POST['tiktok']
        if 'linkedin' in request.POST:
            user.profile.linkedin = request.POST['linkedin']
        if 'website' in request.POST:
            user.profile.website = request.POST['website']

        user.profile.save()
        messages.add_message(
            request,
            messages.INFO,
            'Socials Updated!')
        return redirect('myprofile')


# Attributes to update
@login_required
def updateattributes(request):
    if request.POST:
        user = request.user
        print(request.POST)

        for att in request.POST:
            # if att has a value
            if request.POST[att] != '':
                user.profile.__dict__[att] = request.POST[att]
                user.profile.save()

        user.profile.save()
        messages.add_message(
            request,
            messages.INFO,
            'Attributes Updated!')
        return redirect('myprofile')


# Delete Account and purge data
@login_required
def deleteaccount(request):
    user = request.user
    user.delete()
    messages.add_message(
        request,
        messages.ERROR,
        'Account Deleted!')
    return redirect('account_login')
