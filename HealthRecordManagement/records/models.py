from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    eth_address = models.CharField(max_length=42, unique=True)  # Ethereum address
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    eth_address = models.CharField(max_length=42, unique=True)
    specialty = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    
class HealthRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.CharField(max_length=42)  # Changed from ForeignKey
    record_hash = models.CharField(max_length=66)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record for {self.patient} by {self.doctor_id}"