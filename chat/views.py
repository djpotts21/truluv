from django.shortcuts import render
from chat.models import Message
from myprofile.models import Profile
from likes.models import UserLike
from django.contrib.auth.models import User


def get_chate_user(request, selected_user):
    ''' Get pmessages from current user and the user they are chatting with '''
    # Get all users
    users = Profile.objects.all()
    # Get the current user
    current_user = request.user
    current_user_id = current_user.id
    # if user likes other user and other user likes them
    # add to match list
    matched_users = []
    likes = UserLike.objects.filter(user=current_user)
    for like in likes:
        if UserLike.objects.filter(user=like.liked_user,
                                   liked_user=current_user):

            if Profile.objects.get(id=like.liked_user.id).image1:
                image1 = Profile.objects.get(id=like.liked_user.id).image1
                image1 = image1.url
            else:
                image1 = 'https://i.ibb.co/ssFD4BX/no-image.png'
            age = Profile.objects.get(user=like.liked_user).age
            first_name = User.objects.get(id=like.liked_user.id).first_name
            matched_user_dict = {
                'id': like.liked_user.id,
                'first_name': first_name,
                'image1': image1,
                'age': age
            }
            matched_users.append(matched_user_dict)
    # Get the user they are chatting with from the url argument if
    # selected_user exists
    if selected_user:
        selected_user = selected_user
    else:
        selected_user = None

    # get pmessages to detect new pmessages for session user
    message_alert = list(Message.objects.filter(
        receiver=current_user, read=False))

    # get pmessages for selected user
    pmessages = "None"
    if selected_user:
        sent_pmessages = Message.objects.filter(
            sender=current_user, receiver=selected_user)
        received_pmessages = Message.objects.filter(
            sender=selected_user, receiver=current_user)
        pmessages = list(sent_pmessages.values()) + list(
            received_pmessages.values())
        pmessages.sort(key=lambda x: x["timestamp"])
        # mark message as read for session user
        sent_pmessages.update(read=True)
    else:
        pmessages = "None"
    # render chat template
    return render(request, 'chat/chat.html', {
        'selected_user': selected_user,
        'pmessages': pmessages,
        'selected_user': selected_user,
        'message_alert': message_alert,
        'current_user': current_user,
        'current_user_id': current_user_id,
        'users': users,
        'matched_users': matched_users})


def render_chat_no_user(request):
    ''' Get pmessages from current user and the user they are chatting with '''
    # Get the current user
    current_user = request.user
    current_user_id = current_user.id
    # if user likes other user and other user likes them
    # add to match list
    matched_users = []
    likes = UserLike.objects.filter(user=current_user)
    for like in likes:
        if UserLike.objects.filter(user=like.liked_user,
                                   liked_user=current_user):

            if Profile.objects.get(id=like.liked_user.id).image1:
                image1 = Profile.objects.get(id=like.liked_user.id).image1
                image1 = image1.url
            else:
                image1 = 'https://i.ibb.co/ssFD4BX/no-image.png'
            age = Profile.objects.get(user=like.liked_user).age
            first_name = User.objects.get(id=like.liked_user.id).first_name
            matched_user_dict = {
                'id': like.liked_user.id,
                'first_name': first_name,
                'image1': image1,
                'age': age
            }
            matched_users.append(matched_user_dict)

    return render(request, 'chat/chat.html',
                  {'likes':  likes,
                   'current_user': current_user,
                   'matched_users': matched_users,
                   'current_user_id': current_user_id,
                   })
