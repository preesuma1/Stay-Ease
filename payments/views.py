from django.shortcuts import redirect
from django.conf import settings
from .services import initiate_khalti_payment
from .models import Payment
from bookings.models import Booking


def pay_booking(request, booking_id):

    booking = Booking.objects.get(
        id=booking_id
    )

    response = initiate_khalti_payment(
        amount=booking.total_price,
        booking_id=booking.id,
        customer_name=request.user.username,
        customer_email=request.user.email,
        customer_phone="9800000001",
    )

    payment = Payment.objects.create(
        booking=booking,
        amount=booking.total_price,
        pidx=response["pidx"]
    )

    return redirect(
        response["payment_url"]
    )