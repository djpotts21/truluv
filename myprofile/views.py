from django.shortcuts import render, redirect
import os

# Create your views here.


def myprofile(request):
    # Google API Key for Maps on Profile
    gmapsapikey = os.environ.get('GOOGLE_MAPS_API_KEY')
    print(gmapsapikey)
    return render(request, 'myprofile/myprofile.html', {
        'gmapsapikey': gmapsapikey
    })


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


def updatephone(request):
    if request.POST:
        user = request.user
        user.profile.phone = request.POST['phone']
        user.profile.save()
        return redirect('myprofile')


def updateage(request):
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


def updatelocation(request):
    if request.POST:
        user = request.user
        user.profile.location = request.POST['location']
        user.profile.save()
        return redirect('myprofile')


def resetlocation(request):
    user = request.user
    user.profile.location = None
    user.profile.save()
    return redirect('myprofile')


def updatebio(request):
    if request.POST:
        user = request.user
        user.profile.bio = request.POST['bio']
        user.profile.save()
        return redirect('myprofile')
    

def updategender(request):
    if request.POST:
        user = request.user
        user.profile.gender = request.POST['gender']
        user.profile.save()
        return redirect('myprofile')
    

def updatepronouns(request):
    if request.POST:
        user = request.user
        user.profile.pronouns = request.POST['pronouns']
        user.profile.save()
        return redirect('myprofile')


def updatejobtitle(request):
    if request.POST:
        user = request.user
        user.profile.job_title = request.POST['job_title']
        user.profile.save()
        return redirect('myprofile')
    

def updateeducation(request):
    if request.POST:
        user = request.user
        user.profile.education = request.POST['education']
        user.profile.save()
        return redirect('myprofile')