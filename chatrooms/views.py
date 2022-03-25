from django.shortcuts import render
from .models import ChatRoom, ChatMessage
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def rooms(request):

    all_rooms = ChatRoom.objects.all()

    context = {
        'chat_rooms': all_rooms,
    }

    return render(request, 'chatrooms/rooms.html', context)

@login_required
def chatroom(request, slug):

    room = ChatRoom.objects.get(slug=slug)

    messages = ChatMessage.objects.filter(room=room)[0:25]

    context = {
        'chatroom': room,
        'messages': messages,
    }

    return render(request, 'chatrooms/chatroom.html', context)