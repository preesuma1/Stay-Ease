# from django.db import models
# from django.contrib.auth.models import User
# from properties.models import Property


# class Conversation(models.Model):
#     property = models.ForeignKey(Property, on_delete=models.CASCADE)
#     guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name="guest_chats")
#     host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="host_chats")
#     created_at = models.DateTimeField(auto_now_add=True)


# class Message(models.Model):
#     conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
#     sender = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)