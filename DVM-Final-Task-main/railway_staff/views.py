from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import StationForm, TrainForm
from django.shortcuts import get_object_or_404
from .models import Train, TrainSchedule, PassengerInformation, Booking
from django.core.management import call_command
from importlib import reload
from railway_staff import models
from passengers.models import Complaint

from django.http import HttpResponse
from django.views import View
from openpyxl import Workbook
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test


def is_railway_admin(user):
    return user.groups.filter(name='railway_admin').exists()


def not_authorized(request):
    return render(request, 'railway_staff/not_authorized.html')


def railway_staff_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            # Redirect to a specific page after successful login
            return redirect('railway_staff_dashboard')  # Replace with your dashboard URL name
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'railway_staff/railway_staff_login.html')  # Render the login form


@user_passes_test(is_railway_admin, login_url='not_authorized')
def railway_staff_dash(request):
    return render(request, 'railway_staff/railway_staff_dash.html')


@user_passes_test(is_railway_admin, login_url='not_authorized')
def add_trains(request):
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Train Added Successfully')
            return redirect('add_train')  # Redirect to a success page after saving the train
    else:
        form = TrainForm()

    return render(request, 'railway_staff/add_train.html', {'form': form})


@user_passes_test(is_railway_admin, login_url='railway_staff_login')
def add_station(request):
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            reload(models)
            call_command('makemigrations')
            call_command('migrate')
            messages.success(request, 'Station Added Successfully')
            return redirect('add_station')
    else:
        form = StationForm()

    return render(request, 'railway_staff/add_station.html', {'form': form})


@user_passes_test(is_railway_admin, login_url='railway_staff_login')
def train_schedules(request):
    running_trains = TrainSchedule.objects.all()
    return render(request, 'railway_staff/train_schedules.html', {
        'running_trains': running_trains,
    })


@user_passes_test(is_railway_admin, login_url='railway_staff_login')
def update_trains(request):
    trains = Train.objects.all()  # Retrieve all trains
    show_form = False
    selected_train = None
    form = None

    if request.method == 'GET':
        train_id = request.GET.get('train_id')
        if train_id:
            selected_train = get_object_or_404(Train, pk=train_id)
            form = TrainForm(instance=selected_train)
            show_form = True

    if request.method == 'POST':
        train_id = request.POST.get('train_id')
        selected_train = get_object_or_404(Train, pk=train_id)
        if 'action' in request.POST:
            if request.POST['action'] == 'button1':
                form = TrainForm(request.POST, instance=selected_train)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Train Updated Successfully')
                    return redirect('update_trains')  # Redirect to a success page after updating the train
            elif request.POST['action'] == 'button2':
                selected_train.delete()
                messages.success(request, 'Train Deleted Successfully')
                return redirect('update_trains')

    return render(request, 'railway_staff/update_trains.html', {
        'trains': trains,
        'show_form': show_form,
        'selected_train': selected_train,
        'form': form,
    })


class ExportReservationsView(View):
    def post(self, request, *args, **kwargs):
        train_schedule_id = request.POST.get('selected_schedule')
        train_sch = get_object_or_404(TrainSchedule, id=train_schedule_id)

        reservations_data = Booking.objects.filter(train_sch=train_sch)

        wb = Workbook()
        ws = wb.active

        headers = ['Booking ID', 'Booked By', 'Passenger Name', 'Passenger Email', 'Seat Type', 'Seat no.', 'Train Name', 'Departure Date', 'Fare Per-Head', 'Is Cancelled']
        ws.append(headers)

        for data in reservations_data:
            passenger_info_list = PassengerInformation.objects.filter(booking=data)

            for passenger in passenger_info_list:
                reservation_data = [
                    data.id,
                    data.passenger.user.username,
                    passenger.passenger_name,
                    passenger.passenger_email,
                    passenger.seat_type,
                    passenger.seat_no,
                    data.train.train_name,
                    data.train_sch.departure_date,  # Use train_schedule departure_date
                    data.total_fare / data.num_of_passengers,
                    data.is_cancelled
                ]
                ws.append(reservation_data)

        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=reservations.xlsx'

        wb.save(response)

        return response


@user_passes_test(is_railway_admin, login_url='railway_staff_login')
def complaints(request):
    all_complaint = Complaint.objects.all()
    return render(request, 'railway_staff/complaints.html', {
        'all_complaint': all_complaint,
    })


@user_passes_test(is_railway_admin, login_url='railway_staff_login')
def mark_complaint_viewed(request, complaint_id):
    complaint = get_object_or_404(Complaint, pk=complaint_id)
    complaint.status = True
    complaint.save()
    return HttpResponseRedirect(reverse('complaints'))
