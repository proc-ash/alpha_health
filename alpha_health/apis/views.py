from datetime import datetime

from django.contrib.auth.models import Group

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .permissions import AdminPermission, DoctorPermission, PatientPermission


from apps.base.models import *
from .serializer import DoctorSerializer, PatientSerializer, AppointmentsSerializer

@api_view(['POST'])
def create_auth_token(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()

    auth_token = None
    if user.password == password:
        auth_token, created = Token.objects.get_or_create(user=user)
    return Response({"token" : auth_token.key})
    

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([AdminPermission])
def createDoctor(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response([serializer.errors[error][0] for error in serializer.errors])
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([AdminPermission])
def createPatient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response([serializer.errors[error][0] for error in serializer.errors])
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([AdminPermission])
def createAppointments(request):
    serializer = AppointmentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response([serializer.errors[error][0] for error in serializer.errors])
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def viewDoctorProfile(request):
    doctor_id = request.GET.get('id')
    doctor = Doctor.objects.get(id=doctor_id)
    serializer = DoctorSerializer(doctor)    
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def viewPatientProfile(request):
    is_patient = request.user.groups.all().filter(name='Patient')
    if is_patient and request.user.id != int(patient_id):
        return Response({"Unauthorized Access"})
    patient_id = request.GET.get('id')
    patient = Patient.objects.get(id=patient_id)

    serializer = PatientSerializer(patient)    
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def viewAppointment(request):
    is_doctor = request.user.groups.all().filter(name="Doctor")
    is_patient = request.user.groups.all().filter(name="Patient")

    appointment_id = request.GET.get('id')
    appointment = Appointment.objects.get(id=appointment_id)
    if is_doctor and request.user.id!=appointment.doctor.id or is_patient and request.user.id!=appointment.patient.id:
        return Response({"Unauthorized Access"})

    serializer = AppointmentsSerializer(appointment)    
    return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([AdminPermission])
def updatePatientProfile(request):
    data=request.data
    patient = Patient.objects.get(id=data.get('id',""))
    patient.first_name = data.get('first_name', patient.first_name)
    patient.last_name = data.get('last_name', patient.last_name)
    patient.phone_number = data.get('phone_number', patient.phone_number)
    patient.save()
    serializer = PatientSerializer(patient)    
    return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([AdminPermission])
def updateAppointmentProfile(request):
    data=request.data
    appointment = Appointment.objects.get(id=data.get('id', ''))

    if "appointment_date" in data:
        appointment.appointment_date = datetime.strptime(data.get('appointment_date'), "%Y-%m-%d").date()
    if "from_time" in data:
        appointment.from_time = datetime.strptime(data.get('from_time'), "%H:%M").time()
    if "to_time" in data:
        appointment.to_time = datetime.strptime(data.get('to_time'), "%H:%M").time()

    appointment.save()
    serializer = AppointmentsSerializer(appointment)    
    return Response(serializer.data)
