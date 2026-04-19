from django.urls import path
from chat.api.v1.views import ConversationView, MessageView

urlpatterns = [
    path("conversations/", ConversationView.as_view(), name="conversation-list"),
    path("messages/", MessageView.as_view(), name="message-list"),
]