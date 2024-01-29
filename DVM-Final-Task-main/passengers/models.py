from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # For using built-in User model if needed
from django.conf import settings


class PassengerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_balance = models.DecimalField(max_digits=30, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Complaint(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='complaint_images', blank=True, null=True)
    date_complaint = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)  # Adding 'status' field as BooleanField, whether our complaint is viewed or not

    def __str__(self):
        return f"{self.id} - Status: {self.status}"
