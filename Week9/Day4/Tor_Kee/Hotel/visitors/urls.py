from django.urls import path
from . import views
from .views import HotelDetailView, VacancyListView, BookingCreateView, InquiryCreateView, create_review, booking_success, review_success, available_dates, contact

app_name = 'visitors'

urlpatterns = [
    path('', views.info_page, name='info-page'),
    path('hotels/<int:pk>/', views.HotelDetailView, name='hotel-detail' ),
    path('vacancies/', views.VacancyListView, name='vacancy-list'),
    path('bookings/create/', views.BookingCreateView, name='booking-create'),
    path('inquiries/create/', views.InquiryCreateView, name='inquiry-create'),
    path('reviews/create/', views.create_review, name='review-create'),
    path('booking-success/', views.booking_success, name='booking-success'),
    path('review-success/', views.review_success, name='review-success'),
    path('available-dates/', available_dates, name='available_dates'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
