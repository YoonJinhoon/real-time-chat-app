from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)  # 보낸 사용자와의 관계


class ChatRoom(models.Model):
    room_name = models.CharField(max_length=100)
    participants = models.ManyToManyField(User)
    messages = models.ManyToManyField(Message)  # 메시지 모델과의 관계

    def __str__(self):
        return self.room_name