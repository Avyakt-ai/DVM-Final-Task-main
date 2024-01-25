from django import forms
from .models import Train, Station


class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        exclude = ['available_seats']  # Exclude 'available_seats' from the form


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['station_name']
