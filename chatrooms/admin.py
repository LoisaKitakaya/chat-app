from django.contrib import admin
from .models import ChatRoom, ChatMessage

# Register your models here.

class ChatRoomView(admin.ModelAdmin):

    list_display = ['name', 'slug']

admin.site.register(ChatRoom, ChatRoomView)

class ChatMessageView(admin.ModelAdmin):

    list_display = ['user', 'room', 'date_added']
    list_filter = ['user', 'room', 'date_added']

admin.site.register(ChatMessage, ChatMessageView)