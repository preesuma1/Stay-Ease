from django.urls import path
from payments.api.v1.views import PaymentView
urlpatterns = [
    path("payments/", PaymentView.as_view(), name="payment-list"),
]