"""
URL configuration for truluv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.myprofile, name='myprofile'),
    path('updatename/', views.updatename, name='updatename'),
    path('updateusername/', views.updateusername, name='updateusername'),
    path('updateaddress/', views.updateaddress, name='updateaddress'),
    path('updatephone/', views.updatephone, name='updatephone'),
    path('updateage/', views.updateage, name='updateage'),
    path('uploadphotos/', views.uploadphotos, name='uploadphotos'),
    path('removeimage/', views.removeimage, name='removeimage'),
    path('updatelocation/', views.updatelocation, name='updatelocation'),
    path('resetlocation/', views.resetlocation, name='resetlocation'),
    path('updatebio/', views.updatebio, name='updatebio'),
    path('updateattributes/', views.updateattributes, name='updateattributes'),
    path('updatesocials/', views.updatesocials, name='updatesocials'),
    path('deleteaccount/', views.deleteaccount, name='deleteaccount'),
]
