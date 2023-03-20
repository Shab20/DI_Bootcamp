from django.urls import path
from . import views
from .views import staff, review_list, booking_create, booking_delete, booking_detail, booking_list, booking_success, booking_update, available_dates

app_name = 'staff'

urlpatterns = [
    path('', views.staff, name='staff'),
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

    # Avilaible dates
        path('available-dates/', available_dates, name='available_dates'),
]
