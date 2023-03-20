from django import forms
from .models import Booking, Contact


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'email', 'check_in', 'check_out', 'hotel')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')