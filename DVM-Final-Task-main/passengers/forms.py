from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from railway_staff.models import *

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class BookingForm(forms.Form):
    num_of_passengers = forms.IntegerField(min_value=1, label='Number of Passengers')


class AddMoneyForm(forms.Form):
    amount_added = forms.IntegerField(min_value=0, label='Amount To Be Added')


class PassengerInformationForm(forms.ModelForm):
    class Meta:
        model = PassengerInformation
        fields = ['passenger_name', 'passenger_email']  # Update the fields based on your model
        widgets = {
            'passenger_name': forms.TextInput(attrs={'required': True}),
            'passenger_email': forms.EmailInput(attrs={'required': True}),
            # Add more fields for other passenger details as needed
        }


class UpdatePassengerInformaitonForm(forms.ModelForm):
    class Meta:
        model = PassengerInformation
        exclude = ['booking', 'seat_no', 'seat_type']


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['description', 'image']