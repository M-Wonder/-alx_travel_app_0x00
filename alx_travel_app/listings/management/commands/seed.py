# alx_travel_app/listings/management/commands/seed.py
import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing

User = get_user_model()


class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        if Listing.objects.exists():
            self.stdout.write(self.style.WARNING("Listings already seeded. Skipping..."))
            return

        host, _ = User.objects.get_or_create(
            username="host1",
            defaults={"email": "host1@example.com", "password": "password123"}
        )

        sample_listings = [
            {"title": "Beachfront Villa", "description": "Beautiful villa near the ocean.",
             "location": "Mombasa", "price_per_night": 150.00},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains.",
             "location": "Mt. Kenya", "price_per_night": 90.00},
            {"title": "City Apartment", "description": "Modern apartment in Nairobi CBD.",
             "location": "Nairobi", "price_per_night": 120.00},
        ]

        for data in sample_listings:
            Listing.objects.create(host=host, **data)

        self.stdout.write(self.style.SUCCESS("Seed data created successfully!"))
