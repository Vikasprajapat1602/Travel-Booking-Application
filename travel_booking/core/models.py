from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# travels options
class TravelOption(models.Model):
    TRAVEL_TYPES = [
        ('Flight', 'Flight'),
        ('Train', 'Train'),
        ('Bus', 'Bus'),
    ]

    travel_type = models.CharField(max_length=20, choices=TRAVEL_TYPES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.travel_type}: {self.source} → {self.destination} on {self.date_time}"
    

#  booking model
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Confirmed')

    def __str__(self):
        return f"Booking {self.id} by {self.user.username} - {self.status}"
