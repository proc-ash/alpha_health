from rest_framework import serializers
from apps.base.models import *
from datetime import datetime

class DoctorSerializer(serializers.ModelSerializer): 
    def to_internal_value(self, data):
        data['dob'] = datetime.strptime(data['dob'],"%Y/%m/%d").date()
        return super(DoctorSerializer, self).to_internal_value(data)
    
    def to_representation(self, instance):
        representation = super(DoctorSerializer, self).to_representation(instance)
        doctor_profile = {
            "Name": instance.get_full_name(),
            "Speciality": representation.get('speciality'),
            "Years of Practice": representation.get('years_of_practice'),
            "Phone-number": representation.get('phone_number')
        }
        return doctor_profile

    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer): 
    def to_internal_value(self, data):
        data['dob'] = datetime.strptime(data['dob'],"%Y/%m/%d").date()
        return super(PatientSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        representation = super(PatientSerializer, self).to_representation(instance)
        patient_profile = {
            "Name": instance.get_full_name(),
            "Disease": representation.get('diseases'),
            "Phone-number": representation.get('phone_number')
        }
        return patient_profile

    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentsSerializer(serializers.ModelSerializer): 
    def to_internal_value(self, data):
        data['appointment_date'] = datetime.strptime(data['appointment_date'],"%Y/%m/%d").date()
        data['from_time'] = datetime.strptime(data['from_time'],"%H:%M").time()
        data['from_time'] = datetime.strptime(data['to_time'],"%H:%M").time()

        return super(AppointmentsSerializer, self).to_internal_value(data)

    class Meta:
        model = Appointment
        fields = '__all__'