from django.contrib import admin
from .models import UserReview, PropertyReview

@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    list_display = ["reviewer", "reviewee", "rating", "created_at"]
    list_filter = ["rating"]
    search_fields = ["reviewer__username", "reviewee__username"]

@admin.register(PropertyReview)
class PropertyReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "property", "rating", "created_at"]
    list_filter = ["rating"]
    search_fields = ["user__username", "property__title"]