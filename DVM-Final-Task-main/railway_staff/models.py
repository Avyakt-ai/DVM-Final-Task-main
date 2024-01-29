from django.db import models
from django.utils import timezone


class Station(models.Model):
    station_name = models.CharField(max_length=100)

    def __str__(self):
        return self.station_name


# Here train is treated like a journey, that means that if we have a train named 1A going from A to B on monday at 8am and the same train is coming back to A at 9am then these two train is treated as different.
class Train(models.Model):
    # station_choices = [(item.station_name, item.station_name) for item in Station.objects.all()]
    train_name = models.CharField(max_length=50)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    departure_station = models.CharField(max_length=100)  # choices=station_choices
    destination_station = models.CharField(max_length=100)
    departure_time = models.TimeField(default=timezone.now)
    reaching_time = models.TimeField(default=timezone.now)
    general_fare = models.DecimalField(default=80, max_digits=8, decimal_places=2)
    sleeper_fare = models.DecimalField(default=120, max_digits=8, decimal_places=2)
    third_ac_fare = models.DecimalField(default=200, max_digits=8, decimal_places=2)
    second_ac_fare = models.DecimalField(default=250, max_digits=8, decimal_places=2)
    first_ac_fare = models.DecimalField(default=300, max_digits=8, decimal_places=2)
    available_seats = models.IntegerField(default=50)  # Remove this field from here

    def __str__(self):
        return f"{self.train_name} - {self.departure_station} to {self.destination_station}  at {self.departure_time}"


class TrainSchedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    departure_date = models.DateField(default=timezone.now)
    arrival_date = models.DateField(default=timezone.now)
    available_seats = models.IntegerField(default=0)


class Booking(models.Model):
    passenger = models.ForeignKey('passengers.PassengerProfile', on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    train_sch = models.ForeignKey(TrainSchedule, default=None, on_delete=models.CASCADE)
    departure_date = models.DateField(default=timezone.now)
    num_of_passengers = models.PositiveIntegerField()
    total_fare = models.DecimalField(max_digits=8, decimal_places=2)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking {self.id} by {self.passenger.user.username} on {self.train.train_name}"


class PassengerInformation(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.CharField(max_length=100, null=True)
    seat_type = models.CharField(max_length=100, null=True)
    seat_no = models.BigIntegerField(null=True)

    def __str__(self):
        return f"{self.passenger_name} - Booking: {self.booking.id}"
