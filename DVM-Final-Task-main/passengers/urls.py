from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('login/', views.passenger_login, name='passenger_login'),
    path('dash/', views.passenger_dash, name='passenger_dashboard'),
    path('register/', views.passenger_register, name='passenger_register'),
    path('search_trains/', views.search_trains, name='search_trains'),
    path('book_ticket/', views.book_ticket, name='book_ticket'),
    path('account/', views.account_page, name='account_page'),
    path('your_bookings/', views.your_bookings_page, name='your_bookings'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking_view, name='cancel_booking'),
    path('update_passengers/<int:booking_id>/', views.update_passengers, name='update_passengers'),
    path('download_booking/', views.generate_pdf_view, name='download_booking'),
    path('compaint', views.file_complaint, name='file_complaint'),
]
