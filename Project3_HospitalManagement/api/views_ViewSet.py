from rest_framework import viewsets, status 
from rest_framework.response import Response 
from rest_framework.decorators import action 
from .models import Patient, Doctor, Appointment, MedicalRecord, Billing 
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, MedicalRecordSerializer, BillingSerializer 

class PatientViewSet(viewsets.ViewSet):
    def list(self, request):
        patients = Patient.objects.all() 
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try: 
            patient = Patient.objects.get(pk = pk)
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk=None):
        try:
            patient = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        try:
            # patient = Patient.objects.filter(pk=pk)
            patient = Patient.objects.get(pk=pk)
            patient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class DoctorViewSet(viewsets.ViewSet):
    def list(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    def retrieve(self, request, pk=None):
        try:
            doctor = Doctor.objects.get(pk=pk)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            doctor = Doctor.objects.get(pk=pk)
            serializer = DoctorSerializer(doctor, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def destory(self, request, pk=None):
        try:
            doctor = Doctor.objects.get(pk=pk)
            doctor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class AppointmentViewSet(viewsets.ViewSet):
    def list(self, request):
        appointment = Appointment.objects.all()
        serializer = AppointmentSerializer(appointment, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def create(self, request):
        serializer = AppointmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            appointment = Appointment.objects.get(pk=pk)
            serializer = AppointmentSerializer(appointment) 
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def update(self, request, pk=None):
        try:
            appointment = Appointment.objects.get(pk=pk)
            serializer = AppointmentSerializer(appointment, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)            

    def destroy(self, request, pk=None):
        try:
            appointment = Appointment.objects.get(pk=pk)
            appointment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class MedicalRecordViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            medicalrecords = MedicalRecord.objects.all()
            serializer = MedicalRecordSerializer(medicalrecords, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except MedicalRecord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        try:
            serializer = MedicalRecordSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MedicalRecord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request, pk=None):
        try:
            medicalrecord = MedicalRecord.objects.get(pk=pk)
            serializer = MedicalRecordSerializer(medicalrecord)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MedicalRecord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            medicalrecord = MedicalRecord.objects.get(pk=pk)
            serializer = MedicalRecordSerializer(medicalrecord, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MedicalRecord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    def destroy(self, request, pk=None):
        medicalrecord = MedicalRecord.objects.get(pk=pk)
        medicalrecord.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class BillingViewSet(viewsets.ViewSet):
    def list(self, request):
        billing = Billing.objects.all()
        serializer = BillingSerializer(billing, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            serializer = BillingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Billing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        try:
            billing = Billing.objects.get(pk=pk)
            serializer = BillingSerializer(billing)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Billing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            billing = Billing.objects.get(pk=pk)
            serializer = BillingSerializer(billing, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Billing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        billing = Billing.objects.get(pk=pk)
        billing.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    