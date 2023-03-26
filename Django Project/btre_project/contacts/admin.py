from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'listing', 'contact_date')
    list_display_links = ('name', 'email')
    search_fields = ('name', 'email', 'listing')

# TODO: To register all Apps FIXME:
# from django.apps import apps

# models = apps.get_models()
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.AlreadyRegistered:
#         pass
