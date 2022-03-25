from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatRoom(models.Model):

    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:

        return self.name

class ChatMessage(models.Model):

    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['date_added']

    def __str__(self) -> str:
        
        return self.user
