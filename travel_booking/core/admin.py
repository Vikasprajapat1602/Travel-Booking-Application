from django.contrib import admin
from .models import TravelOption
from .models import Booking

# Register your models here.

@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ('travel_type', 'source', 'destination', 'date_time', 'price', 'available_seats')
    list_filter = ('travel_type', 'source', 'destination')
    search_fields = ('source', 'destination')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'travel_option', 'number_of_seats', 'total_price', 'status', 'booking_date')
    list_filter = ('status',)
    search_fields = ('user__username', 'travel_option__source', 'travel_option__destination')
