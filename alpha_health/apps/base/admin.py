from django.contrib import admin
from .models import Appointment, Patient, Doctor, Admin

#Register your models here.
@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
   list_display = ('id', 'doctor', 'patient',)

@admin.register(Doctor)
class Doctor(admin.ModelAdmin):
  list_display = ('id', 'username')

@admin.register(Patient)
class Patient(admin.ModelAdmin):
  list_display = ('id', 'username')

@admin.register(Admin)
class Patient(admin.ModelAdmin):
  list_display = ('id', 'username')