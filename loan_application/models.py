from django.db import models
from car_listing.models import CarListing

class LoanApplication(models.Model):
    APPLICANT_TYPES = [
        ('applicant', 'Applicant'),
        ('co_applicant', 'Co-Applicant'),
    ]
    car_name = models.ForeignKey(
        CarListing,
        on_delete=models.PROTECT,
        related_name="loan_applications",
        help_text="Which car this application is for"
    )
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    dob_or_registerdate = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    marital_status = models.CharField(max_length=50)
    sin = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=50)
    address_duration = models.CharField(max_length=50)
    home_ownership = models.CharField(max_length=50)

    applicant_type = models.CharField(
        max_length=20, choices=APPLICANT_TYPES, default='applicant'
    )

    parent_applicant = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='co_applicants',
        help_text="Link to the main applicant if this is a co-applicant"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class EmploymentInfo(models.Model):
    loan_application = models.OneToOneField(LoanApplication, on_delete=models.CASCADE, related_name="employment_info")
    business_name = models.CharField(max_length=255)
    length_of_employment = models.IntegerField()
    street_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    gross_monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    company_number = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.business_name} - {self.position}"
