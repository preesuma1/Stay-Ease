from django.contrib import admin
from .models import Property, PropertyImage

# Register your models here.


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["title", "host", "property_type", "price_per_night", "is_active"]
    list_filter = ["property_type", "is_active"]
    search_fields = ["title", "location", "host__username"]

    inlines = [PropertyImageInline]


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ["property", "image"]


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1
