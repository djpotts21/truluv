from django.shortcuts import render

# Create your views here.


def myprofile(request):
    return render(request, 'myprofile/myprofile.html', {})