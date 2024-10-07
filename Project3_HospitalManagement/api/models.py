from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length = 255)
    dob = models.DateField() 
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return f"{self.name}"

class Doctor(models.Model):
    name = models.CharField(max_length = 255)
    specialization = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 14)

    def __str__(self):
        return f"{self.name}-{self.specialization}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()

    def __str__(self):
        return f"{self.patient.name}'s Doc {self.doctor.name}"
    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.patient.name} - {self.notes[:15]}..."
    
