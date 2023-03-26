from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'realtor', 'city', 'price', 'is_published', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'city', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': ('realtor', 'title', 'address', 'city', 'state', 'zipcode', 'description', 'price')
        }),
        ('Property Details', {
            'fields': ('bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size')
        }),
        ('Photos', {
            'fields': ('photo_main', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6')
        }),
        ('Listing Status', {
            'fields': ('is_published',)
        }),
        ('Listing Date', {
            'fields': ('list_date',)
        })
    )
