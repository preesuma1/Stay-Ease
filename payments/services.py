import requests

from django.conf import settings


def initiate_khalti_payment(
    amount,
    booking_id,
    customer_name,
    customer_email,
    customer_phone,
):
    payload = {
        "return_url":
        "http://127.0.0.1:8000/payments/verify/",

        "website_url":
        "http://127.0.0.1:8000",

        "amount": int(amount * 100),

        "purchase_order_id":
        str(booking_id),

        "purchase_order_name":
        f"Booking {booking_id}",

        "customer_info": {
            "name": customer_name,
            "email": customer_email,
            "phone": customer_phone,
        }
    }

    headers = {
        "Authorization":
        f"Key {settings.KHALTI_SECRET_KEY}",
        "Content-Type":
        "application/json",
    }

    response = requests.post(
        settings.KHALTI_INITIATE_URL,
        json=payload,
        headers=headers
    )

    return response.json()