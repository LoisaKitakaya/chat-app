from .models import ChatRoom

def chat_rooms(request):

    rooms = ChatRoom.objects.all()

    return {
        'chat_rooms': rooms,
    }