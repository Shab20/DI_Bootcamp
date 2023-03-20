from django.urls import path
from . import views
from .views import HotelDetailView, VacancyListView, InquiryCreateView, create_review, booking_success, available_dates, contact
from .views import booking_list, booking_create, booking_detail, booking_delete, booking_success, booking_update
from .views import contact, contact_success, review_list

app_name = 'visitors'

urlpatterns = [ 
    path('', views.info_page, name='info-page'),

    # Reviews
    path('staff/reviews', views.review_list, name='review_list'),
    path('review-success/', views.review_success, name='review-success'),

    # Bookings
    path('bookinglist', views.booking_list, name='booking_list'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
    path('createbooking/', views.booking_create, name='booking_create'),
    path('<int:pk>/update/', views.booking_update, name='booking_update'),
    path('<int:pk>/delete/', views.booking_delete, name='booking_delete'),
    path('booking-success/', views.booking_success, name='booking-success'),

    path('reviews/create/', views.create_review, name='review-create'),

    path('hotels/<int:pk>/', views.HotelDetailView, name='hotel-detail' ),
    path('vacancies/', views.VacancyListView, name='vacancy-list'),
    path('inquiries/create/', views.InquiryCreateView, name='inquiry-create'),

    path('available-dates/', available_dates, name='available_dates'),

    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
