import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        # Create host users if none exist
        if not User.objects.filter(is_staff=False).exists():
            for _ in range(5):
                User.objects.create_user(
                    username=fake.user_name(),
                    email=fake.email(),
                    password='password123'
                )
            self.stdout.write(self.style.SUCCESS('Created 5 host users.'))

        hosts = User.objects.filter(is_staff=False)

        # Create listings
        for _ in range(20):
            Listing.objects.create(
                name=fake.company(),
                description=fake.text(),
                price_per_night=random.randint(50, 500),
                host=random.choice(hosts)
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded 20 listings.'))
