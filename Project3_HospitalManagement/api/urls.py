from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from .views import PatientViewSet, DoctorViewSet, AppointmentViewSet, MedicalRecordViewSet, BillingViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointment', AppointmentViewSet)
router.register(r'medical_records', MedicalRecordViewSet)
router.register(r'billing', BillingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]