# -alx_travel_app_0x00

This project is a Django-based travel booking platform.

## Setup

1. Install dependencies:
   ```bash
   pip install django djangorestframework

Apply migrations:

python manage.py makemigrations
python manage.py migrate


Run the development server:

python manage.py runserver


Seed the database with sample data:

python manage.py seed

Features

Listings for properties (title, description, location, price per night).

Bookings with status (pending, confirmed, canceled).

Reviews with ratings and comments.

REST API serialization for Listings and Bookings.


---

✅ Now you have **models, serializers, a seeder, and project documentation** ready.  

Would you like me to also add **ViewSets + URLs** so you can expose Listings and Bookings via API immediately?
