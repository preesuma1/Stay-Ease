from django.contrib import admin
from .models import Conversation, Message

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ["property", "guest", "host", "created_at"]
    search_fields = ["guest__username", "host__username", "property__title"]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["conversation", "sender", "is_read", "created_at"]
    list_filter = ["is_read"]
    search_fields = ["sender__username", "text"]