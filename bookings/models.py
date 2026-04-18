from django.db import models
from django.contrib.auth.models import User
from properties.models import Property
# Create your models here.

class BookingStatus(models.TextChoices):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"

class Booking(models.Model):
    guest = models.ForeignKey(User, on_delete = models.CASCADE)
    property = models.ForeignKey(Property, on_delete = models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits = 10, decimal_places=2)
    status = models.CharField(max_length = 20, choices = BookingStatus.choices, default = BookingStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.guest.username} - {self.property.title}"