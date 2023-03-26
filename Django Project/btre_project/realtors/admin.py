from django.contrib import admin
from .models import Realtor

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'is_MVP', 'hire_date')
    list_display_links = ('id', 'name')
    list_filter = ('is_MVP', 'hire_date')
    list_editable = ('is_MVP',)
    search_fields = ('name', 'email', 'phone')
    list_per_page = 25

# admin.site.register(Realtor, RealtorAdmin)
