from django.shortcuts import render,redirect
from chat.models import Message
from myprofile.models import Profile


def send_message(request):
    if request.method == 'POST':
        sender = request.user
        receiver = request.POST.get('receiver')
        message = request.POST.get('message')
        Message.objects.create(sender=sender, receiver=receiver, message=message)
        return redirect('chat')


def get_messages(user):
    sender = user
    receiver = user
    message_data = {}
    all_messages_list = []
    messages = Message.objects.filter(
        sender=sender) | Message.objects.filter(
            receiver=receiver)
    print(messages)
    for message in messages.order_by('timestamp'):
        sender_profile = Profile.objects.get(user=message.sender)
        receiver_profile = Profile.objects.get(user=message.receiver)
        message_data = {
            'sender': message.sender,
            'sender_profile': sender_profile,
            'receiver': message.receiver,
            'receiver_profile': receiver_profile,
            'message': message.message,
            'read': message.read,
            'read_at': message.read_at,
            'timestamp': message.timestamp,
        }
        all_messages_list.append(message_data)
    return all_messages_list


def view_chat(request):
    user = request.user
    all_messages = get_messages(user)
    return render(request, 'chat/chat.html', {
        'message_data': all_messages,
    })