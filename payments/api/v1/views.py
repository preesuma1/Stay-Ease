import requests

from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema

from payments.models import Payment
from bookings.models import Booking
from .serializers import PaymentSerializer


class PaymentListView(GenericAPIView):

    @extend_schema(tags=["Payments"])
    def get(self, request):
        payments = Payment.objects.all()
        return Response(PaymentSerializer(payments, many=True).data)

class InitiatePaymentView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=["Payments"])
    def post(self, request, booking_id):

        booking = get_object_or_404(Booking, id=booking_id)

        # prevent double payment
        if hasattr(booking, "payment") and booking.payment.status == "COMPLETED":
            return Response({"error": "Already paid"}, status=400)

        payload = {
            "return_url": "http://127.0.0.1:8000/api/payments/verify/",
            "website_url": "http://127.0.0.1:8000",

            "amount": int(booking.total_price * 100),

            "purchase_order_id": str(booking.id),
            "purchase_order_name": f"Booking {booking.id}",

            "customer_info": {
                "name": request.user.username,
                "email": request.user.email,
                "phone": "9800000000"
            }
        }

        headers = {
            "Authorization": f"Key {settings.KHALTI_SECRET_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            settings.KHALTI_INITIATE_URL,
            json=payload,
            headers=headers
        )

        data = response.json()

        if "pidx" not in data:
            return Response({"error": "Khalti initiation failed"}, status=400)

        Payment.objects.create(
            booking=booking,
            amount=booking.total_price,
            pidx=data["pidx"],
            status="PENDING"
        )

        return Response({
            "payment_url": data["payment_url"],
            "pidx": data["pidx"]
        })
    
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