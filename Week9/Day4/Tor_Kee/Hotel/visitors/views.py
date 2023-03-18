from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Hotel, Availability, Booking, Inquiry, Review, BookingForm, InquiryForm, ReviewForm
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.mail import send_mail
from django.urls import reverse

def info_page(request):
    return render(request, 'info_page.html')

def HotelDetailView(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    context = {'hotel': hotel}
    return render(request, 'hotel_detail.html', context)

def VacancyListView(request):
    vacancies = Availability.objects.all()
    context = {'vacancies': vacancies}
    return render(request, 'vacancy_list.html', context)

@csrf_exempt
def BookingCreateView(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been successful!')
            # return redirect('booking-success')
    else:
        form = BookingForm()

    context = {
        'form': form,
    }

    return render(request, 'booking_form.html', context)

@csrf_exempt
def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been successful!')
            # return redirect('booking-success')
    else:
        form = BookingForm()

    context = {'form': form}
    return render(request, 'booking_form.html', context)

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

def booking_success(request):
    context = {}
    return render(request, 'booking_success.html', context)

def review_success(request):
    context = {}
    return render(request, 'review_success.html', context)

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


def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            'Contact form submission',
            f'Email: {email}\nMessage: {message}',
            email,
            ['your_email@example.com'],
            fail_silently=False,
        )
        return redirect(reverse('contact_success'))
    return render(request, 'contact.html')

def contact_success(request):
    return render(request, 'contact_success.html')