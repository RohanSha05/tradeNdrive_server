# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
# from django.conf import settings
# from .models import LoanApplication, EmploymentInfo
# from io import BytesIO
# from xhtml2pdf import pisa
# from django.db import transaction

# @api_view(['POST'])
# def submit_loan_application(request):
#     data = request.data
    
#     required_fields = [
#         "car_name","first_name", "last_name", "dob_or_registerdate", "phone", "email",
#         "marital_status", "postal_code", "sin", "street_name",
#         "city", "province", "address_duration", "home_ownership",
#         "business_name", "emp_street_name", "emp_province", "emp_postal_code",
#         "emp_city", "length_of_employment", "position", "department",
#         "gross_monthly_income", "company_number"
#     ]

#     missing_fields = [field for field in required_fields if not data.get(field)]
    
#     if data.get("co_applicant") == "yes":
#         co_applicant_fields = [f"co_{field}" for field in required_fields]
#         missing_fields += [field for field in co_applicant_fields if not data.get(field)]
    
#     if missing_fields:
#         return Response({
#             "status": "error",
#             "message": "Missing required fields.",
#             "missing_fields": missing_fields
#         }, status=400)

#     try:
#         with transaction.atomic():
#             loan_application = LoanApplication.objects.create(
#                 car_name=data.get('car_name'),
#                 first_name=data.get('first_name'),
#                 middle_name=data.get('middle_name', None),
#                 last_name=data.get('last_name'),
#                 dob_or_registerdate=data.get('dob_or_registerdate'),
#                 phone=data.get('phone'),
#                 email=data.get('email'),
#                 marital_status=data.get('marital_status'),
#                 postal_code=data.get('postal_code'),
#                 sin=data.get('sin'),
#                 street_name=data.get('street_name'),
#                 city=data.get('city'),
#                 province=data.get('province'),
#                 address_duration=data.get('address_duration'),
#                 home_ownership=data.get('home_ownership'),
#                 applicant_type='applicant',
#             )

#             employment_info = EmploymentInfo.objects.create(
#                 loan_application=loan_application,
#                 business_name=data.get('business_name'),
#                 street_name=data.get('emp_street_name'),
#                 province=data.get('emp_province'),
#                 postal_code=data.get('emp_postal_code'),
#                 city=data.get('emp_city'),
#                 length_of_employment=data.get('length_of_employment'),
#                 position=data.get('position'),
#                 department=data.get('department'),
#                 gross_monthly_income=data.get('gross_monthly_income'),
#                 company_number=data.get('company_number'),
#             )

#             co_loan_application = None
#             co_employment_info = None
            
#             if data.get("co_applicant") == "yes":
#                 co_loan_application = LoanApplication.objects.create(
#                     first_name=data.get('co_first_name'),
#                     middle_name=data.get('co_middle_name', None),
#                     last_name=data.get('co_last_name'),
#                     dob_or_registerdate=data.get('co_dob_or_registerdate'),
#                     phone=data.get('co_phone'),
#                     email=data.get('co_email'),
#                     marital_status=data.get('co_marital_status'),
#                     postal_code=data.get('co_postal_code'),
#                     sin=data.get('co_sin'),
#                     street_name=data.get('co_street_name'),
#                     city=data.get('co_city'),
#                     province=data.get('co_province'),
#                     address_duration=data.get('co_address_duration'),
#                     home_ownership=data.get('co_home_ownership'),
#                     applicant_type='co-applicant',
#                     parent_applicant=loan_application,
#                 )

#                 co_employment_info = EmploymentInfo.objects.create(
#                     loan_application=co_loan_application,
#                     business_name=data.get('co_business_name'),
#                     street_name=data.get('co_emp_street_name'),
#                     province=data.get('co_emp_province'),
#                     postal_code=data.get('co_emp_postal_code'),
#                     city=data.get('co_emp_city'),
#                     length_of_employment=data.get('co_length_of_employment'),
#                     position=data.get('co_position'),
#                     department=data.get('co_department'),
#                     gross_monthly_income=data.get('co_gross_monthly_income'),
#                     company_number=data.get('co_company_number'),
#                 )

#         def generate_pdf(html_content):
#             pdf_file = BytesIO()
#             pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)
#             if pisa_status.err:
#                 return None
#             pdf_file.seek(0)
#             return pdf_file.read()

#         html_content = render_to_string('loan_application/loan_template.html', {'applicant': loan_application, 'employment': employment_info})
#         applicant_pdf = generate_pdf(html_content)
        
#         co_applicant_pdf = None
#         if co_loan_application:
#             co_html_content = render_to_string('loan_application/co_applicant.html', {'main_applicant': loan_application, 'applicant': co_loan_application, 'employment': co_employment_info})
#             co_applicant_pdf = generate_pdf(co_html_content)
        
#         applicant_name = f"{loan_application.first_name} {loan_application.last_name}"

#         email_subject = f"Isam Auto Credit Application - {applicant_name}"
#         if co_loan_application:
#             email_subject = f"Isam Auto Credit Application with Co Applicant - {applicant_name}"


#         email_body = f"""
#         Dear {loan_application.first_name} {loan_application.last_name},

#         Thank you for submitting your credit application to Isam Auto. 

#         We have successfully received your application, and our team will review it shortly.
#         A copy of your completed application form is attached for your records. If we require any additional information, 
#         we will contact you at the provided details.

#         If you have any questions or need further assistance, please feel free to reach out.

#         Best regards,  
#         Isam Auto Team  
#         📞 Contact: +1 306-974-4820  
#         📧 Email: contact@isamauto.ca
#         📍 Address: 1009 20th St W, Saskatoon, SK S7M 0Y6, Canada  
#         🌐 Website: isamauto.ca
#         """
        
#         recipients = [loan_application.email, "gallantdigital360@gmail.com"]
#         cc_recipients = []

#         if co_loan_application and co_loan_application.email:
#             cc_recipients.append(co_loan_application.email)

#         email = EmailMessage(
#             subject=email_subject,
#             body=email_body,
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             to=recipients,
#             cc=cc_recipients
#         )

#         email.attach('loan_application.pdf', applicant_pdf, 'application/pdf')
        
#         if co_applicant_pdf:
#             email.attach('co_applicant_loan_application.pdf', co_applicant_pdf, 'application/pdf')

#         try:
#             email.send()
#         except Exception as e:
#             return Response({"status": "error", "message": "Failed to send email.", "error": str(e)}, status=500)

#         return Response({
#             "status": "success",
#             "message": "Successfully submitted your application.",
#             "application_id": loan_application.id,
#             "applicant_name": f"{loan_application.first_name} {loan_application.last_name}",
#             "applicant_email": loan_application.email
#         }, status=201)

#     except Exception as e:
#         return Response({"status": "error", "message": "An error occurred while processing your application.", "error": str(e)}, status=500)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.db import transaction
from io import BytesIO
from xhtml2pdf import pisa

from car_listing.models import CarListing
from .models import LoanApplication, EmploymentInfo

@api_view(['POST'])
def submit_loan_application(request):
    data = request.data

    # 1) Ensure car_id is provided
    car_id = data.get('car_id')
    if not car_id:
        return Response({
            "status": "error",
            "message": "Missing required field: car_id"
        }, status=400)

    # 2) Lookup the CarListing
    try:
        car = CarListing.objects.get(pk=car_id)
    except CarListing.DoesNotExist:
        return Response({
            "status": "error",
            "message": f"Invalid car_id: {car_id}"
        }, status=400)

    # 3) Check all other required fields
    required = [
        "first_name", "last_name", "dob_or_registerdate",
        "phone", "email", "marital_status", "postal_code", "sin",
        "street_name", "city", "province", "address_duration",
        "home_ownership", "business_name", "emp_street_name",
        "emp_city", "emp_province", "emp_postal_code",
        "length_of_employment", "position", "department",
        "gross_monthly_income", "company_number"
    ]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return Response({
            "status": "error",
            "message": "Missing required fields.",
            "missing_fields": missing
        }, status=400)

    try:
        with transaction.atomic():
            # 4) Create the LoanApplication, using car.title
            loan_app = LoanApplication.objects.create(
                car_name=car.title,
                first_name=data['first_name'],
                middle_name=data.get('middle_name'),
                last_name=data['last_name'],
                dob_or_registerdate=data['dob_or_registerdate'],
                phone=data['phone'],
                email=data['email'],
                marital_status=data['marital_status'],
                sin=data['sin'],
                street_name=data['street_name'],
                city=data['city'],
                province=data['province'],
                postal_code=data['postal_code'],
                address_duration=data['address_duration'],
                home_ownership=data['home_ownership'],
                applicant_type='applicant'
            )

            emp = EmploymentInfo.objects.create(
                loan_application=loan_app,
                business_name=data['business_name'],
                street_name=data['emp_street_name'],
                city=data['emp_city'],
                province=data['emp_province'],
                postal_code=data['emp_postal_code'],
                length_of_employment=data['length_of_employment'],
                position=data['position'],
                department=data['department'],
                gross_monthly_income=data['gross_monthly_income'],
                company_number=data['company_number']
            )

            # (Optional) handle co-applicant exactly as before…
            co_app = None
            co_emp = None
            if data.get("co_applicant") == "yes":
                co_app = LoanApplication.objects.create(
                    car_name=car.title,                  # same car
                    first_name=data['co_first_name'],
                    middle_name=data.get('co_middle_name'),
                    last_name=data['co_last_name'],
                    dob_or_registerdate=data['co_dob_or_registerdate'],
                    phone=data['co_phone'],
                    email=data['co_email'],
                    marital_status=data['co_marital_status'],
                    sin=data['co_sin'],
                    street_name=data['co_street_name'],
                    city=data['co_city'],
                    province=data['co_province'],
                    postal_code=data['co_postal_code'],
                    address_duration=data['co_address_duration'],
                    home_ownership=data['co_home_ownership'],
                    applicant_type='co-applicant',
                    parent_applicant=loan_app
                )
                co_emp = EmploymentInfo.objects.create(
                    loan_application=co_app,
                    business_name=data['co_business_name'],
                    street_name=data['co_emp_street_name'],
                    city=data['co_emp_city'],
                    province=data['co_emp_province'],
                    postal_code=data['co_emp_postal_code'],
                    length_of_employment=data['co_length_of_employment'],
                    position=data['co_position'],
                    department=data['co_department'],
                    gross_monthly_income=data['co_gross_monthly_income'],
                    company_number=data['co_company_number']
                )

        # 5) PDF generation util
        def generate_pdf(html_content):
            buffer = BytesIO()
            pisa_status = pisa.CreatePDF(html_content, dest=buffer)
            if pisa_status.err:
                return None
            buffer.seek(0)
            return buffer.read()

        # 6) Render templates (pass car into context if needed)
        html_main = render_to_string(
            'loan_application/loan_template.html',
            {
                'applicant': loan_app,
                'employment': emp,
                'car': car
            }
        )
        pdf_main = generate_pdf(html_main)

        pdf_co = None
        if co_app:
            html_co = render_to_string(
                'loan_application/co_applicant.html',
                {
                    'main_applicant': loan_app,
                    'applicant': co_app,
                    'employment': co_emp,
                    'car': car
                }
            )
            pdf_co = generate_pdf(html_co)

        # 7) Email creation
        applicant_name = f"{loan_app.first_name} {loan_app.last_name}"
        subject = f"Isam Auto Credit Application – {car.title} for {applicant_name}"
        body = render_to_string(
            'loan_application/email_body.txt',
            {'applicant': loan_app, 'car': car}
        )

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[loan_app.email, "gallantdigital360@gmail.com"],
            cc=[co_app.email] if co_app else []
        )
        email.attach('loan_application.pdf', pdf_main, 'application/pdf')
        if pdf_co:
            email.attach('co_applicant_loan_application.pdf', pdf_co, 'application/pdf')

        email.send(fail_silently=False)

        return Response({
            "status": "success",
            "message": "Application submitted—check your e-mail!",
            "application_id": loan_app.id
        }, status=201)

    except Exception as exc:
        return Response({
            "status": "error",
            "message": "Failed to process application",
            "error": str(exc)
        }, status=500)
