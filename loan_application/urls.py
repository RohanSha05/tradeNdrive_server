from django.urls import path
from loan_application.views import *

urlpatterns = [
    path('loan-application/', submit_loan_application, name='loan_application'),
]
