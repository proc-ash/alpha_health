from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser


# Create your models here.

# class AlphaHealthUser(models.Model):

#     first_name = models.CharField(User, on_delete=models.CASCADE)
#     last_name = models.CharField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=13, blank=False,unique=True )
#     email = models.EmailField(unique=True, blank=False)
#     password = models.CharField(('password'), max_length=128)
#     address = models.CharField(max_length=30, blank=True)
#     dob = models.DateField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Gender(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

class Status(models.Model):
    APPOINTMENT_STATUS = [
        ('B', 'Booked'),
        ('A', 'Approved'),
        ('C', 'Cancelled')
    ]

class Admin(User):
    phone_number = models.CharField(max_length=13, unique=True)
    address = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, choices=Gender.GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'alpha_admin'
        verbose_name_plural = 'alpha_admins'


class Patient(User):
    phone_number = models.CharField(max_length=13, unique=True)
    address = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, choices=Gender.GENDER_CHOICES)
    dob = models.DateField(null=True, blank=True)
    diseases = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'alpha_patient'
        verbose_name_plural = 'alpha_patients'


class Doctor(User):
    phone_number = models.CharField(max_length=13, unique=True)
    address = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, choices=Gender.GENDER_CHOICES, default=Gender.GENDER_CHOICES[0])
    dob = models.DateField(null=True, blank=True)
    speciality = models.CharField(max_length=50, null=False)
    last_degree = models.CharField(max_length=100)
    years_of_practice = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_full_name()
    
    class Meta:
        verbose_name = 'alpha_doctor'
        verbose_name_plural = 'alpha_doctors'

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=Status.APPOINTMENT_STATUS)
    cancalled_reason = models.TextField(max_length=255)

    def __str__(self):
        return self.patient.get_full_name()
    
    class Meta:
        verbose_name = 'appointment'
        verbose_name_plural = 'appointments'

