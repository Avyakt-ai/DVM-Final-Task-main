from django.contrib import admin
from django.urls import path, include
from . import views
from passengers import views as passengers_views

# I set the below namespace in order to use the url of this app into the template of passengers app(template: type_of_user.html) but it just work without all this shit.
# app_name = 'railway_staff'

urlpatterns = [
    path('login/', views.railway_staff_login, name='railway_staff_login'),
    path('dash/', views.railway_staff_dash, name='railway_staff_dashboard'),
    path('add_train/', views.add_trains, name='add_train'),
    path('add_station/', views.add_station, name='add_station'),
    path('update_train/', views.update_trains, name='update_trains'),
    path('train_schedules/', views.train_schedules, name='train_schedules'),
    path('export_excel/', views.ExportReservationsView.as_view(), name='export_excel'),
    path('complaints', views.complaints, name='complaints'),
    path('complaint/<int:complaint_id>/mark_viewed/', views.mark_complaint_viewed, name='mark_complaint_viewed'),
    path('not_authorized/', views.not_authorized, name='not_authorized')
]
