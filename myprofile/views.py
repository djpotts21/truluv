from django.shortcuts import render, redirect

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
        print(user.profile.address)
        user.profile.address = request.POST['address']
        print("----")
        print(request.POST['address'])
        user.profile.save()
        return redirect('myprofile')


def updateaboutme(request):
    if request.POST:
        user = request.user
        user.profile.age = request.POST['age']
        user.profile.save()
        return redirect('myprofile')
