from django.db import models
from django import forms

class Availability(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.hotel} ({self.date})'

    class Meta:
        verbose_name_plural = 'Availabilities'
        unique_together = ('hotel', 'date')

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Hotels'

class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    
class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.IntegerField()
    name = models.CharField(max_length=20, null=True)
    comment = models.TextField()
    

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['id','hotel', 'rating','name','comment']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'email', 'check_in', 'check_out', 'hotel']

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'message']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


