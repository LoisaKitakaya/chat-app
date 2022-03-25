from django.contrib import admin
from .models import ChatRoom

# Register your models here.

class ChatRoomView(admin.ModelAdmin):

    list_display = ['name', 'slug']

admin.site.register(ChatRoom, ChatRoomView)