
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("createDoctor/", views.createDoctor),
    path("createPatient/", views.createPatient),
    path("createAppointments/", views.createAppointments),
    path("viewDoctorProfile/", views.viewDoctorProfile),
    path("viewPatientProfile/", views.viewPatientProfile),
    path("viewAppointment/", views.viewAppointment),
    path('updatePatientProfile/',views.updatePatientProfile),
    path('updateAppointmentProfile/',views.updateAppointmentProfile),
    path('create_auth_token/', views.create_auth_token),
]

