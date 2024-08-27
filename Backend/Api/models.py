from django.db import models
from Accounts.models import User, DoctorProfile, PatientProfile
from django.utils import timezone

class Appointment(models.Model):
    APPOINTMENT_TYPES = [
        ('Physical', 'Physical'),
        ('Zoom', 'Zoom'),
    ]

    APPOINTMENT_STATUS = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    doctor = models.ForeignKey('Accounts.DoctorProfile', on_delete=models.CASCADE)
    patient = models.ForeignKey('Accounts.PatientProfile', on_delete=models.CASCADE)
    appointment_type = models.CharField(choices=APPOINTMENT_TYPES, default='Zoom' ,max_length=10)
    scheduled_time = models.DateTimeField()
    status = models.CharField(choices=APPOINTMENT_STATUS, default='Scheduled', max_length=15)
    zoom_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.user.get_full_name} and {self.patient.user.get_full_name} on {self.scheduled_time}"
    

class MedicalRecord(models.Model):
    patient = models.ForeignKey('Accounts.PatientProfile', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Accounts.DoctorProfile', on_delete=models.CASCADE)
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
    notes = models.TextField()
    prescriptions = models.TextField()
    diagnosis = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medical Record for {self.patient.user.get_full_name} by Dr. {self.doctor.user.get_full_name} on {self.date_created}"


class Payment(models.Model):
    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed')
    ]

    patient = models.ForeignKey('Accounts.PatientProfile', on_delete=models.CASCADE)
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(choices=PAYMENT_STATUS, default='Pending', max_length=12)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment of {self.amount} by {self.patient.user.get_full_name} for appointment on {self.appointment.scheduled_time}"


class Review(models.Model):
    doctor = models.ForeignKey('Accounts.DoctorProfile', on_delete=models.CASCADE)
    patient = models.ForeignKey('Accounts.PatientProfile', on_delete=models.CASCADE)
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.patient.user.get_full_name} for {self.doctor.user.get_full_name} - {self.rating} Stars"