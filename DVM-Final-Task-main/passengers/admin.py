from django.contrib import admin

# Register your models here.
from .models import PassengerProfile, Complaint

admin.site.register(PassengerProfile)
admin.site.register(Complaint)
