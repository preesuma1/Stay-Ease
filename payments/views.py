import requests

from django.http import HttpResponse

from django.conf import settings

from .models import Payment


def verify_payment(request):

    pidx = request.GET.get("pidx")

    headers = {
        "Authorization":
        f"Key {settings.KHALTI_SECRET_KEY}"
    }

    response = requests.post(
        settings.KHALTI_LOOKUP_URL,
        json={"pidx": pidx},
        headers=headers
    )

    data = response.json()

    payment = Payment.objects.get(
        pidx=pidx
    )

    if data["status"] == "Completed":

        payment.status = "COMPLETED"
        payment.transaction_id = data["transaction_id"]
        payment.save()

        booking = payment.booking
        booking.is_paid = True
        booking.save()

        return HttpResponse(
            "Payment Successful"
        )

    payment.status = "FAILED"
    payment.save()

    return HttpResponse(
        "Payment Failed"
    )