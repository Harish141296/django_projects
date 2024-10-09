from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import PatientAPIView, PatientDetailAPIView, DoctorAPIView, DoctorDetailAPIView, AppointmentAPIView, AppointmentDetailAPIView, MedicalRecordAPIView, MedicalRecordDetailAPIView, BillingAPIView, BillingDetailAPIView 

urlpatterns = [
    path('patients/', PatientAPIView.as_view(), name='patient-list'),
    path('patients/<int:pk>', PatientDetailAPIView.as_view(), name='patient-detail'),
    path('doctors/', DoctorAPIView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/',DoctorDetailAPIView.as_view(), name='doctor-detail'),
    path('appointments/', AppointmentAPIView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>', AppointmentDetailAPIView.as_view(), name='appointment-detail'),
    path('medical_records/', MedicalRecordAPIView.as_view(), name='medicalrecord-list'),
    path('medical_records/<int:pk>', MedicalRecordDetailAPIView.as_view(), name='medicalrecord-detail'),
    path('billings/', BillingAPIView.as_view(), name='billing-list'),
    path('billing/<int:pk>', BillingDetailAPIView.as_view(), name='billing-detail'),

]