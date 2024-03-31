from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_chat_no_user, name='render_chat_no_user'),
    path('user/<int:selected_user>/',
         views.get_chate_user, name='get_chate_user'),
    ]
