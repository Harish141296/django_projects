from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import BillingViewSet, AppointmentViewSet, MedicalRecordViewSet, DoctorViewSet, PatientViewSet 

router = DefaultRouter()
router.register(r'patients',PatientViewSet, basename='patient')
router.register(r'doctor', DoctorViewSet, basename='doctor')
router.register(r'appointment', AppointmentViewSet, basename='appointment')
router.register(r'medical_record',MedicalRecordViewSet, basename='medicalrecord')
router.register(r'billing', BillingViewSet, basename='billing')

urlpatterns = [
    path('', include(router.urls)),
]