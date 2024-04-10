from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from myprofile.models import Profile
from likes.models import UserLike
from chat.models import Message
from checkuserpremium.models import check_user_premium
from django.contrib import messages



@login_required
def send_message(request, selected_user):
    # Run premium user check
    check_user_premium(request)

    if request.method == 'POST':
        ''' Send a message from the current user to the selected user '''
        # Get the current user
        current_user = request.user
        # Get the selected user
        selected_user = User.objects.get(id=selected_user)
        selected_user_id = selected_user.id
        # Assign Names
        sender_name = current_user.first_name
        receiver_name = selected_user.first_name
        # Get the message
        message = request.POST.get('message')
        # Create the message
        Message.objects.create(
            sender=current_user, receiver=selected_user,
            message=message, sender_name=sender_name,
            receiver_name=receiver_name)
        # Redirect to the chat page
    messages.add_message(
        request,
        messages.INFO,
        'Message has been sent.')
    return redirect('get_chate_user', selected_user=selected_user_id)


@login_required
def flag_message(request, message_id):

    # Get the message
    message = Message.objects.get(id=message_id)

    if request.method == 'POST':
        ''' Flag a message as inappropriate '''
        message_id = int(message_id)
        # Flag the message
        message.flagged = True
        message.save()
        # Redirect to the chat page

    print("Redirecting")
    messages.add_message(
        request,
        messages.INFO,
        'Message has been flagged as inappropriate.')
    return redirect('get_chate_user', selected_user=message.sender.id)


@login_required
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

            if Profile.objects.get(user=like.liked_user).image1:
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

    # count number of flagged messages from selected user to current user
    # or current user to selected user
    flagged_messages_to_current_user = Message.objects.filter(
        sender=selected_user, receiver=current_user, flagged=True).count()
    flagged_messages_from_current_user = Message.objects.filter(
        sender=current_user, receiver=selected_user, flagged=True).count()
    flagged_messages = flagged_messages_to_current_user + \
        flagged_messages_from_current_user

    # is current user a premium user?
    current_user = request.user
    current_user_profile = Profile.objects.get(user=current_user)
    premium_status = current_user_profile.premium_user_account

    # get all messages for selected user and create
    # dictioary for each unique receiver containing the message,
    # timestamp, sender, receiver
    messages = Message.objects.filter(sender=current_user)
    premium_message_dict = {}
    for message in messages:
        if message.receiver.id not in premium_message_dict:
            profile_data = get_object_or_404(Profile, user=message.sender)
            if profile_data.image1:
                image1 = profile_data.image1.url
            else:
                image1 = 'https://i.ibb.co/ssFD4BX/no-image.png'
            premium_message_dict[message.receiver.id] = {
                'receiver': message.receiver.id,
                'message': message.message,
                'timestamp': message.timestamp,
                'sender': message.sender.id,
                'sender_name': message.sender_name,
                'receiver_name': message.receiver_name,
                'user_image': image1
            }

    # matched users
    matched_users = []
    likes = UserLike.objects.filter(user=current_user)
    for like in likes:
        if UserLike.objects.filter(user=like.liked_user,
                                   liked_user=current_user):

            if Profile.objects.get(user=like.liked_user).image1:
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

    # Get Selected User First Name
    selected_user_fname = User.objects.get(id=selected_user)
    selected_user_fname = selected_user_fname.first_name

    # Get all Messages for request user
    amessages = Message.objects.filter(receiver=request.user)


    # render chat template
    return render(request, 'chat/chat.html', {
        'selected_user_fname': selected_user_fname,
        'selected_user': selected_user,
        'pmessages': pmessages,
        'message_alert': message_alert,
        'current_user': current_user,
        'current_user_id': current_user_id,
        'users': users,
        'matched_users': matched_users,
        'flagged_messages': flagged_messages,
        'premium_status': premium_status,
        'premium_message_dict': premium_message_dict,
        'amessages': amessages, })


@login_required
def render_chat_no_user(request):
    # Run premium user check
    check_user_premium(request)

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
            if Profile.objects.get(user=like.liked_user).image1:
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

    # is current user a premium user?
    current_user = request.user
    current_user_profile = Profile.objects.get(user=current_user)
    premium_status = current_user_profile.premium_user_account

    # get all messages for selected user and create dictioary
    # for each unique receiver containing the message, timestamp,
    # sender, receiver
    messages = Message.objects.filter(sender=current_user)
    premium_message_dict = {}
    for message in messages:
        if message.receiver.id not in premium_message_dict:
            premium_message_dict[message.receiver.id] = {
                'receiver': message.receiver.id,
                'message': message.message,
                'timestamp': message.timestamp,
                'sender': message.sender.id,
                'sender_name': message.sender_name,
                'receiver_name': message.receiver_name,
                'user_image': image1
            }

    # Get all Messages for request user
    amessages = Message.objects.filter(receiver=request.user)

    return render(request, 'chat/chat.html',
                  {'likes':  likes,
                   'current_user': current_user,
                   'matched_users': matched_users,
                   'current_user_id': current_user_id,
                   'premium_status': premium_status,
                   'premium_message_dict': premium_message_dict,
                   'amessages': amessages, })


# Check for unread chats
def check_unread_messages(request):
    unread_messages = Message.objects.filter(receiver=request.user, read=False)
    user_profile = Profile.objects.get(user=request.user)
    if len(unread_messages) > 0: 
        if user_profile.premium_user_account is False:
            messages.add_message(
                request,
                messages.INFO,
                'You are not a premium user. Upgrade now to view messages from non-matched users.')
        else:
            messages.add_message(
                request,
                messages.INFO,
                'You have unread messages. Click on the Messeages Icon to view.')

