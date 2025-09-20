# alx_travel_app/listings/models.py
import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Listing(models.Model):
    """Represents a property listing (hotel, house, etc)."""
    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    location = models.CharField(max_length=255, null=False)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hosted_listings")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.location}"


class Booking(models.Model):
    """Represents a booking made by a user for a listing."""
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("canceled", "Canceled")],
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("listing", "user", "start_date", "end_date")

    def __str__(self):
        return f"Booking {self.booking_id} for {self.listing.title} by {self.user}"


class Review(models.Model):
    """Represents a user review for a listing."""
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField()  # enforce between 1-5 in validation
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("listing", "user")

    def __str__(self):
        return f"Review {self.rating}/5 for {self.listing.title} by {self.user}"

