from django.urls import path
from .views import (
    PaymentListView,
    InitiatePaymentView,
    VerifyPaymentView
)

urlpatterns = [
    path("", PaymentListView.as_view(), name="payment-list"),
    path("initiate/<int:booking_id>/", InitiatePaymentView.as_view(), name="payment-initiate"),
    path("verify/", VerifyPaymentView.as_view(), name="payment-verify"),
]