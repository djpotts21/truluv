from django.shortcuts import render

# Create your views here.


def myprofile(request):
    return render(request, 'myprofile/myprofile.html', {})


def updatename(request):
    if request.POST:
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return render(request, 'myprofile/myprofile.html', {})
    

def updateusername(request):
    if request.POST:
        user = request.user
        print(request.POST['username'])
        user.username = request.POST['username']
        user.save()
        return render(request, 'myprofile/myprofile.html', {})
