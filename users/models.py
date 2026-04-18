from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GenderType(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15, null=True, blank=True, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=GenderType.choices, null=True, blank=True
    )
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField()
    language = models.CharField(max_length=20, default="English")
    currency = models.CharField(max_length=10, default="NPR")
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class DocumentType(models.TextChoices):
    PASSPORT = "Passport"
    CITIZENSHIP = "Citizenship"


class VerificationStatus(models.TextChoices):
    PENDING = "Pending"
    VERIFIED = "Verified"
    REJECTED = "Rejected"


class IdentityVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=20, choices=DocumentType.choices)
    document_image = models.ImageField(upload_to="verification/")
    status = models.CharField(
        max_length=10,
        choices=VerificationStatus.choices,
        default=VerificationStatus.PENDING,
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default = "My Wishlist")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    property_id = models.PositiveIntegerField()
    # replace with FK → Property later
    # property = models.ForeignKey("properties.Property", on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wishlist {self.wishlist.id} - Property {self.property_id}"



class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.city}, {self.country}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
