from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Availability
from .models import BookingForm, Booking
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


# staff landing page
def staff(request):
    return render(request, 'staff_home.html')

# Review
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

# bookings
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})


def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking_detail.html', {'booking': booking})


def booking_create(request):
    if request.method == 'POST':
        bookings = Booking.objects.all()
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return render(request, 'booking_list.html', {'bookings': bookings})
            # return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})


def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        bookings = Booking.objects.all()
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save()
            return render(request, 'booking_list.html', {'bookings': bookings})
            # return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_form.html', {'form': form})


def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    # If the request method is not POST, render the template as usual
    return render(request, 'booking_delete.html', {'booking': booking})

def booking_success(request):
    context = {}
    return render(request, 'booking_success.html', context)


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