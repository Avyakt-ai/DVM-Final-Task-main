from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib import admin
from .models import Train

admin.site.register(Train)
admin.site.register(Booking)
admin.site.register(PassengerInformation)
admin.site.register(Station)
admin.site.register(TrainSchedule)
# admin.site.register()

