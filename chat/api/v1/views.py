from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from chat.models import Conversation, Message
from .serializers import *


class ConversationView(GenericAPIView):

    @extend_schema(tags=["Chat"])
    def get(self, request):
        return Response(ConversationSerializer(Conversation.objects.all(), many=True).data)


class MessageView(GenericAPIView):

    @extend_schema(tags=["Chat"])
    def get(self, request):
        return Response(MessageSerializer(Message.objects.all(), many=True).data)