from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_chat_no_user, name='render_chat_no_user'),
    path('user/<int:selected_user>/',
         views.get_chate_user, name='get_chate_user'),
    path('send_message/<int:selected_user>/',
         views.send_message, name='send_message'),
    path('flag_message/<int:message_id>/',
         views.flag_message, name='flag_message'),
    ]
