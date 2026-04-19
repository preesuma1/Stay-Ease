from django.urls import path
from bookings.api.v1.views import BookingView

urlpatterns = [
    path("bookings/", BookingView.as_view(), name="booking-list-create"),
]