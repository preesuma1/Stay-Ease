import requests

from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema

from payments.models import Payment
from bookings.models import Booking
from .serializers import PaymentSerializer


class PaymentListView(GenericAPIView):

    @extend_schema(tags=["Payments"])
    def get(self, request):
        payments = Payment.objects.all()
        return Response(PaymentSerializer(payments, many=True).data)

class PaymentListView(GenericAPIView):

    @extend_schema(tags=["Payments"])
    def get(self, request):
        payments = Payment.objects.all()
        return Response(PaymentSerializer(payments, many=True).data)
    
class VerifyPaymentView(GenericAPIView):

    authentication_classes = []  # IMPORTANT (Khalti has no JWT)
    permission_classes = []      # PUBLIC ENDPOINT

    @extend_schema(tags=["Payments"])
    def get(self, request):

        pidx = request.GET.get("pidx")

        if not pidx:
            return Response({"error": "pidx required"}, status=400)

        headers = {
            "Authorization": f"Key {settings.KHALTI_SECRET_KEY}"
        }

        response = requests.post(
            settings.KHALTI_LOOKUP_URL,
            json={"pidx": pidx},
            headers=headers
        )

        data = response.json()

        payment = get_object_or_404(Payment, pidx=pidx)

        if data.get("status") == "Completed":

            payment.status = "COMPLETED"
            payment.transaction_id = data.get("transaction_id")
            payment.save()

            booking = payment.booking
            booking.is_paid = True
            booking.status = "CONFIRMED"
            booking.save()

            return Response({"message": "Payment successful"})

        payment.status = "FAILED"
        payment.save()

        return Response({"message": "Payment failed"})