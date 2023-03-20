from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Hotel, Availability, Booking, Inquiry, Review, BookingForm, InquiryForm, ReviewForm
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.mail import send_mail
from .forms import ContactForm


# visitors landing page
def info_page(request):
    return render(request, 'info_page.html')


# bookings
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})


def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking_detail.html', {'booking': booking})


def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            # return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})


def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save()
            # return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_form.html', {'form': form})


def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    # return redirect('booking_list')

def booking_success(request):
    context = {}
    return render(request, 'booking_success.html', context)


# hotel details
def HotelDetailView(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    context = {'hotel': hotel}
    return render(request, 'hotel_detail.html', context)

def VacancyListView(request):
    vacancies = Availability.objects.all()
    context = {'vacancies': vacancies}
    return render(request, 'vacancy_list.html', context)

# algorithm for available dates
def available_dates(request):
    today = timezone.now().date()
    bookings = Booking.objects.filter(check_out__gte=today).order_by('check_in')
    booked_dates = set()
    for booking in bookings:
        current_date = booking.check_in
        while current_date <= booking.check_out:
            booked_dates.add(current_date)
            current_date += timezone.timedelta(days=1)

    dates = []
    current_date = today
    while len(dates) < 365:
        if current_date not in booked_dates:
            dates.append(current_date)
        current_date += timezone.timedelta(days=1)

    context = {'dates': dates}
    return render(request, 'available_dates.html', context)

@csrf_exempt
def InquiryCreateView(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been successful!')
            # return redirect('inquiry-success')
    else:
        form = InquiryForm()

    context = {
        'form': form,
    }

    return render(request, 'inquiry_form.html', context)

# reviews 
@csrf_exempt
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been saved!')
            # return redirect('create_review')
    else:
        form = ReviewForm()

    reviews = Review.objects.all()
    return render(request, 'review_form.html', {'form': form, 'reviews': reviews})

def review_list(request):
    reviews = Review.objects.all()
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        review = get_object_or_404(Review, pk=review_id)
        review.delete()
        # return redirect('review_list')
    return render(request, 'staff_review.html', {'reviews': reviews})

def review_success(request):
    context = {}
    return render(request, 'review_success.html', context)

# contact
@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')