# from django.db import models
# from django.contrib.auth.models import User
# from bookings.models import Booking


# class PaymentStatus(models.TextChoices):
#     INITIATED = "Initiated"
#     SUCCESS = "Success"
#     FAILED = "Failed"


# class Payment(models.Model):
#     booking = models.OneToOneField(Booking, on_delete=models.CASCADE)

#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     amount = models.DecimalField(max_digits=10, decimal_places=2)

#     transaction_id = models.CharField(max_length=255, null=True, blank=True)

#     status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.INITIATED)

#     created_at = models.DateTimeField(auto_now_add=True)