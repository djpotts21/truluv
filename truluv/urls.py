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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('myprofile/', include('myprofile.urls')),
    path('viewuser/', include('viewuser.urls')),
    path('likes/', include('likes.urls')),
    path('chat/', include('chat.urls')),
    path('usergrid/', include('usergrid.urls')),
    path('upgradeaccount/', include('upgradeaccount.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
