from rest_framework import serializers
from .models import Patient, Doctor, HealthRecord

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'user', 'eth_address', 'phone']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'user', 'eth_address', 'specialty']

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = ['id', 'patient', 'doctor_id', 'record_hash', 'created_at']  # Updated