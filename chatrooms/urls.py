from unicodedata import name
from django.urls import path
from chatrooms import views

urlpatterns = [
    path('rooms/', views.rooms, name='rooms'),
    path('<slug:slug>/', views.chatroom, name='chatroom'),
]