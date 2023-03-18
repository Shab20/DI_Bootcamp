from django.contrib import admin
from .models import Availability, Hotel, Booking, Inquiry, Review

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'date', 'price')
    list_filter = ('hotel', 'date')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'check_in', 'check_out', 'hotel')
    list_filter = ('hotel',)
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'rating')
    list_filter = ('hotel',)
