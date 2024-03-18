from django.shortcuts import render, redirect
from django.contrib.gis.geoip2 import GeoIP2

# Create your views here.


def myprofile(request):
    return render(request, 'myprofile/myprofile.html', {})


def updatename(request):
    if request.POST:
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return redirect('myprofile')
    

def updateusername(request):
    if request.POST:
        user = request.user
        print(request.POST['username'])
        user.username = request.POST['username']
        user.save()
        return redirect('myprofile')


def updateaddress(request):
    if request.POST:
        user = request.user
        user.profile.address = request.POST['address']
        user.profile.save()
        return redirect('myprofile')


def updateaboutme(request):
    if request.POST:
        user = request.user
        user.profile.age = request.POST['age']
        user.profile.save()
        return redirect('myprofile')


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
        return redirect('myprofile')


def removeimage(request):
    image_id = int(request.GET.get('image_id'))
    print(image_id)
    user = request.user
    if image_id == 1:
        user.profile.image1 = None

    if image_id == 2:
        user.profile.image2 = None

    if image_id == 3:
        user.profile.image3 = None
    
    if image_id == 4:
        user.profile.image4 = None
    
    if image_id == 5:
        user.profile.image5 = None
    
    if image_id == 6:
        user.profile.image6 = None
    
    if image_id == 7:
        user.profile.image7 = None
    
    user.profile.save()
    return redirect('myprofile')
