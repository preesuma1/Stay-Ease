from django.db import models
from django.contrib.auth.models import User
from properties.models import Property
from django.core.exceptions import ValidationError


class UserReview(models.Model):
    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="given_reviews"
    )
    reviewee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_reviews"
    )

    rating = models.PositiveIntegerField()  # 1–5 stars
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("reviewer", "reviewee")

    def __str__(self):
        return f"{self.reviewer.username} → {self.reviewee.username} ({self.rating} stars)"

    def clean(self):
        if self.reviewer == self.reviewee:
            raise ValidationError("You cannot review yourself.")
        if not (1 <= self.rating <= 5):
            raise ValidationError("Rating must be between 1 and 5.")


class PropertyReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    rating = models.PositiveIntegerField()  # 1–5 stars
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "property")

    def __str__(self):
        return f"{self.user.username} → {self.property} ({self.rating} stars)"

    def clean(self):
        if not (1 <= self.rating <= 5):
            raise ValidationError("Rating must be between 1 and 5.")
