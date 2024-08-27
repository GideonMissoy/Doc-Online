from django.urls import path
from .views import *

urlpatterns = [
    path('appointments/', ListAppointmentsView.as_view(), name='list-appointments'),
    path('appointments/create/', CreateAppointmentView.as_view(), name='create-appointment'),
    path('records/create/', CreateMedicalRecordView.as_view(), name='create-record'),
    path('records/<int:pk>/', RetrieveMedicalRecordView.as_view(), name='retrieve-record'),
    path('payments/', ListPaymentView.as_view(), name='list-payments'),
    path('payments/create/', CreatePaymentView.as_view(), name='create-payment'),
    path('payments/<int:pk>/', RetrievePaymentView.as_view(), name='retrieve-payment'),
    path('reviews/create/', CreateReviewView.as_view(), name='create-review'),
    path('reviews/patient/', ListPatientReviewsView.as_view(), name='patient-reviews'),
    path('reviews/doctor/', ListDoctorReviewsView.as_view(), name='doctor-reviews'),
]
