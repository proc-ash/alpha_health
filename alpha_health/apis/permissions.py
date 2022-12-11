
from rest_framework import permissions
from apps.base.models import Admin, Doctor, Patient


class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        is_admin = request.user.groups.all().filter(name='Admin')
        if request.user.is_authenticated and is_admin:
            return True

class DoctorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        is_doctor = request.user.groups.all().filter(name='Doctor')
        if request.user.is_authenticated and is_doctor:
            return True

class PatientPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        is_patient = request.user.groups.all().filter(name='Patient')
        if request.user.is_authenticated and is_patient:
            return True
