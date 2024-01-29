# Register your models here.
from .models import Train, Booking, PassengerInformation, Station, TrainSchedule
from django.contrib import admin

admin.site.register(Train)
admin.site.register(Booking)
admin.site.register(PassengerInformation)
admin.site.register(Station)
admin.site.register(TrainSchedule)
