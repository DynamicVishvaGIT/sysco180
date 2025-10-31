from datetime import datetime
from email import header
import logging
from venv import logger
logger = logging.getLogger(__name__)
from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from syscoapp.models import *

# Create your views here.

def login(request):
    return render(request,'login.html')

def add_user(request):
    return render(request,'add_user.html')

def arbitrator(request):
    return render(request,'arbitrator.html')

def mediator(request):
    return render(request,'mediator.html')

def personal_information(request):
    return render(request,'personal_information.html')

def review(request):
    return render(request,'review.html')

# Arbitrator ----------

def arbitrator_dashboard(request):
    return render(request,'arbitrator/arbitrator_dashboard.html')

def assigned_cases(request):
    return render(request,'arbitrator/assigned_cases.html')

def assigned_cases_view(request):
    return render(request,'arbitrator/assigned_cases_view.html')

def arbitrator_head(request):
    return render(request,'arbitrator/head.html')

def arbitrator_header(request):
    return render(request,'arbitrator/header.html')

def hearings(request):
    return render(request,'arbitrator/hearings.html')

def arbitrator_script(request):
    return render(request,'arbitrator/script.html')

# Bank User -------------------------------------------> 

def bank_user_dashboard(request):
    return render(request,'bank_user/bank_user_dashboard.html')

def my_cases(request):
    return render(request,'bank_user/my_cases.html')

def my_cases_view(request):
    return render(request,'bank_user/my_cases_view.html')

def upload_cases(request):
    return render(request,'bank_user/upload_cases.html')

def bank_user_head(request):
    return render(request,'bank_user/head.html')

def bank_user_script(request):
    return render(request,'bank_user/script.html')

def bank_user_header(request):
    return render(request,'bank_user/header.html')


# Mediator ------------------------------------------->

def mediator_dashboard(request):
    return render(request,'mediator/mediator_dashboard.html')       

def mediator_head(request):
    return render(request,'mediator/head.html')

def mediator_script(request):
    return render(request,'mediator/script.html')

def mediator_header(request):
    return render(request,'mediator/header.html')

def mediation_cases(request):   
    return render(request,'mediator/mediation_cases.html')

def mediation_cases_view(request):   
    return render(request,'mediator/mediation_cases_view.html')

def sessions(request):   
    return render(request,'mediator/sessions.html')


#Sysco Admin ------------------------------------------->

def sysco_admin_dashboard(request):
    return render(request,'sysco_admin/sysco_admin_dashboard.html')

def arbitrators(request):
    return render(request,'sysco_admin/arbitrators.html')

def add_arbitrator(request):
    return render(request,'sysco_admin/add_arbitrator.html')

def arbitrator_view(request):
    return render(request,'sysco_admin/arbitrator_view.html')

def cash_queue(request):
    return render(request,'sysco_admin/cash_queue.html')

def cash_queue_view(request):
    return render(request,'sysco_admin/cash_queue_view.html')

def upload_cases(request):
    return render(request,'sysco_admin/upload_cases.html')

def sysco_admin_header(request):
    return render(request,'sysco_admin/header.html')

def sysco_admin_head(request):
    return render(request,'sysco_admin/head.html')

def sysco_admin_script(request):
    return render(request,'sysco_admin/script.html')

def hearings(request):
    return render(request,'sysco_admin/hearings.html')

def template(request):
    return render(request,'sysco_admin/templates.html')

@csrf_exempt
@api_view(['POST'])
def user_registration(request):
    try:
        user_type = request.POST.get("user_registration_type")
        terms = request.POST.get("terms_and_conditions")
        terms_bool = True if terms and terms.lower() in ["yes", "true", "1", "on"] else False

        logger.info(f'''
            user_type = {user_type}
            terms_bool             =  {terms_bool}

''')
        valid_types = ["mediator", "arbitrator", "bank_individual"]
        if not user_type or user_type.lower() not in valid_types:
            return JsonResponse(
                {"error": f"Invalid user_registration_type '{user_type}' or undefined"},
                status=400
            )

        full_name                       = request.POST.get("full_name")
        date_of_birth                   = request.POST.get("date_of_birth")
        gender                          = request.POST.get("gender")
        nationality                     = request.POST.get("nationality")
        permanent_address               = request.POST.get("permanent_address")
        mobile_no                       = request.POST.get("mobile_no")
        email_id                        = request.POST.get("email_id")
        aadhar_no                       = request.POST.get("aadhar_no")
        passport_no                     = request.POST.get("passport_no")
        current_occupation_designation  = request.POST.get("current_occupation_designation")
        organization_name               = request.POST.get("organization_name")
        office_address                  = request.POST.get("office_address")
        professional_contact_no         = request.POST.get("professional_contact_no")
        official_email_id               = request.POST.get("official_email_id")
        sanad_id                        = request.POST.get("sanad_id")
        website                         = request.POST.get("website")
        qualification                   = request.POST.get("qualification")
        university_name                 = request.POST.get("university_name")
        year_of_passing                 = request.POST.get("year_of_passing")
        specialization                  = request.POST.get("specialization")
        memberships                     = request.POST.get("memberships")
        number_of_arbitrations_conducted = request.POST.get("number_of_arbitrations_conducted")
        sectors_of_experience           = request.POST.get("sectors_of_experience")
        year_of_experience              = request.POST.get("year_of_experience")
        mediation_experience            = request.POST.get("mediation_experience")
        trainings_certifications        = request.POST.get("trainings_certifications")
        area_of_specialization          = request.POST.get("area_of_specialization")
        languages_proficiency           = request.POST.get("languages_proficiency")
        declaration_and_disclosure      = request.POST.get("declaration_and_disclosure")
        declaration_date                = request.POST.get("declaration_date")
        declaration_place               = request.POST.get("declaration_place")
        occupation                       = request.POST.get("occupation")
        professional_contact             = request.POST.get("professional_contact")
        official_email                   = request.POST.get("official_email")
        institution                      = request.POST.get("institution")
        mediation_conducted              = request.POST.get("mediation_conducted")
        sectors_experience               = request.POST.get("sectors_experience")
        years_experience                 = request.POST.get("years_experience")
        trainings                        = request.POST.get("trainings")
        areas_specialization             = request.POST.get("areas_specialization")
        language_proficiency             = request.POST.get("language_proficiency")
        declaration_name                 = request.POST.get("declaration_name")
        name                             = request.POST.get("name")
        contact_no                       = request.POST.get("contact_no")
        state                            = request.POST.get("state")
        city                             = request.POST.get("city")
        pin_code                         = request.POST.get("pin_code")
        address                          = request.POST.get("address")
        updated_cv                       = request.FILES.get("updated_cv")
        id_proof_file                    = request.FILES.get("id_proof_file") or request.FILES.get("photo_id")
        pan_card_file                    = request.FILES.get("pan_card_file") or request.FILES.get("pan_card")
        passport_size_photo_file         = request.FILES.get("passport_size_photo_file") or request.FILES.get("photo")
        education_certification_file     = request.FILES.get("education_certification_file") or request.FILES.get("education_certificates")
        sanad_id_file                    = request.FILES.get("sanad_id_file")
        membership_certification_file    = request.FILES.get("membership_certification_file") or request.FILES.get("membership_certificates")

        def parse_date(date_str):
            try:
                return datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else None
            except ValueError:
                raise ValidationError(f"Invalid date format for {date_str}. Expected YYYY-MM-DD")

        if user_type.lower() == "arbitrator":
            Arbitrator.objects.create(
                USER_TYPE=user_type,
                FULL_NAME=full_name,
                DATE_OF_BIRTH=parse_date(date_of_birth),
                GENDER=gender,
                NATIONALITY=nationality,
                PERMANENT_ADDRESS=permanent_address,
                MOBILE_NO=mobile_no,
                EMAIL_ID=email_id,
                AADHAR_NO=aadhar_no,
                PASSPORT_NO=passport_no,
                CURRENT_OCCUPATION_DESIGNATION=current_occupation_designation,
                ORGANIZATION_NAME=organization_name,
                OFFICE_ADDRESS=office_address,
                PROFESSIONAL_CONTACT_NO=professional_contact_no,
                OFFICIAL_EMAIL_ID=official_email_id,
                SANAD_ID=sanad_id,
                WEBSITE=website,
                QUALIFICATION=qualification,
                UNIVERSITY_NAME=university_name,
                YEAR_OF_PASSING=year_of_passing,
                SPECIALIZATION=specialization,
                MEMBERSHIPS=memberships,
                NUMBER_OF_ARBITRATIONS_CONDUCTED=number_of_arbitrations_conducted,
                SECTORS_OF_EXPERIENCE=sectors_of_experience,
                YEAR_OF_EXPERIENCE=year_of_experience,
                MEDIATION_EXPERIENCE=mediation_experience,
                TRAININGS_CERTIFICATIONS=trainings_certifications,
                AREA_OF_SPECIALIZATION=area_of_specialization,
                LANGUAGES_PROFICIENCY=languages_proficiency,
                DECLARATION_AND_DISCLOSURE=declaration_and_disclosure,
                DECLARATION_DATE=parse_date(declaration_date),
                DECLARATION_PLACE=declaration_place,
                UPDATED_CV=updated_cv,
                ID_PROOF_FILE=id_proof_file,
                PAN_CARD_FILE=pan_card_file,
                PASSPORT_SIZE_PHOTO_FILE=passport_size_photo_file,
                EDUCATION_CERTIFICATION_FILE=education_certification_file,
                SANAD_ID_FILE=sanad_id_file,
                MEMBERSHIP_CERTIFICATION_FILE=membership_certification_file,
                TERMS_AND_CONDITIONS=terms_bool,
            )
            return JsonResponse({"message": "Arbitrator registered successfully","user_type":user_type}, status=201)

        elif user_type.lower() == "mediator":
            Mediator.objects.create(
                USER_TYPE=user_type,
                FULL_NAME=full_name,
                DATE_OF_BIRTH=parse_date(date_of_birth),
                GENDER=gender,
                NATIONALITY=nationality,
                PERMANENT_ADDRESS=permanent_address,
                MOBILE_NO=mobile_no,
                EMAIL_ID=email_id,
                CURRENT_OCCUPATION_DESIGNATION=occupation,
                ORGANIZATION_NAME=organization_name,
                OFFICE_ADDRESS=office_address,
                PROFESSIONAL_CONTACT_NO=professional_contact,
                OFFICIAL_EMAIL_ID=official_email,
                QUALIFICATION=qualification,
                UNIVERSITY_NAME=institution,
                YEAR_OF_PASSING=year_of_passing,
                SPECIALIZATION=specialization,
                MEMBERSHIPS=memberships,
                NUMBER_OF_MEDIATION_CONDUCTED=mediation_conducted,
                SECTORS_OF_EXPERIENCE=sectors_experience,
                YEAR_OF_EXPERIENCE=years_experience,
                MEDIATION_CONCILIATION_EXPERIENCE=mediation_experience,
                TRAININGS_CERTIFICATIONS=trainings,
                AREA_OF_SPECIALIZATION=areas_specialization,
                LANGUAGES_PROFICIENCY=language_proficiency,
                DECLARATION_AND_DISCLOSURE_FULL_NAME=declaration_name,
                DECLARATION_DATE=parse_date(declaration_date),
                DECLARATION_PLACE=declaration_place,
                UPDATED_CV=updated_cv,
                ID_PROOF_FILE=id_proof_file,
                PAN_CARD_FILE=pan_card_file,
                PASSPORT_SIZE_PHOTO_FILE=passport_size_photo_file,
                EDUCATION_CERTIFICATION_FILE=education_certification_file,
                MEMBERSHIP_CERTIFICATION_FILE=membership_certification_file,
                TERMS_AND_CONDITIONS=terms_bool,
            )
            return JsonResponse({"message": "Mediator registered successfully","user_type":user_type}, status=201)

        elif user_type.lower() == "bank_individual":
            Bank_individual_user.objects.create(
                USER_TYPE=user_type,
                FULL_NAME=name,
                EMAIL_ID=email_id,
                CONTACT_NO=contact_no,
                NATIONALITY=nationality,
                STATE=state,
                CITY=city,
                PIN_CODE=pin_code,
                ADDRESS=address,
                PERMANENT_ADDRESS=permanent_address,
                TERMS_AND_CONDITIONS=terms_bool,
            )
            return JsonResponse({"message": "Bank Individual User registered successfully","user_type":user_type}, status=201)

        else:
            return JsonResponse({"error": f"Invalid user_registration_type '{user_type}'"}, status=400)

    except Exception as e:
        logger.exception(e)
        return JsonResponse({"error": "Something went wrong", "details": str(e)}, status=500)





