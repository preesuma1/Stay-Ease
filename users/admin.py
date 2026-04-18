from django.contrib import admin
from .models import (
    UserProfile,
    IdentityVerification,
    Wishlist,
    WishlistItem,
    UserAddress,
    Notification,
)



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["full_name", "user", "is_verified", "contact_number"]
    list_filter = ["is_verified"]
    search_fields = ["full_name", "user__username", "user__email"]


@admin.register(IdentityVerification)
class IdentityVerificationAdmin(admin.ModelAdmin):
    list_display = ["user", "document_type", "status", "submitted_at"]
    list_filter = ["status", "document_type"]
    search_fields = ["user__username"]


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "created_at"]
    search_fields = ["user__username", "name"]


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ["wishlist", "added_at"]
    list_filter = ["wishlist"]


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ["user", "city", "country", "is_default"]
    list_filter = ["country", "is_default"]
    search_fields = ["user__username", "city"]


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "is_read", "created_at"]
    list_filter = ["is_read"]
    search_fields = ["user__username", "title"]
