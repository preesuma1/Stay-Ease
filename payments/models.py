from django.db import models
from django.contrib.auth.models import User
from bookings.models import Booking

class Payment(models.Model):

    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    pidx = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    transaction_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking.id}"