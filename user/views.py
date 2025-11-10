from django.utils.timezone import now
from email import header
import logging
from venv import logger
logger = logging.getLogger(__name__)
from django import apps
from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from user.utils.auth_decorator import custom_authentication
from user.utils.otp_manager import OTPManager
import uuid
from user.models import *
from master.models import StateMaster, CityMaster
from django.apps import apps


# Create your views here.

model_map = {
    'admin': ('user', 'Admin'),
    'arbitrator': ('user', 'Arbitrator'),
    'mediator': ('user', 'Mediator'),
    'bank_individual': ('user', 'Bank_individual_user'),
}

def login(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')

def registration(request):
    return render(request,'signup_signin/registration.html')

def arbitrator(request):
    return render(request,'arbitrator.html')

def mediator(request):
    return render(request,'mediator.html')

def personal_information(request):
    bank_name= BankMaster.objects.filter(IS_DELETED=False)
    return render(request,'personal_information.html',context={"bank_name":bank_name})

def view_details_page(request):
    return render(request,'view_details.html')

# Arbitrator ---------------------------------------------------------------->

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

# Bank User --------------------------------------------------------------------------> 


# Mediator -------------------------------------------------------------------------->

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


#Sysco Admin ------------------------------------------------------------------------------>

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

# def upload_cases(request):
#     return render(request,'sysco_admin/upload_cases.html')

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

@api_view(['POST'])
def user_type(request):
    try:
        user_type  = request.POST.get("user_registration_type")
        terms      = request.POST.get("terms_and_conditions")
        terms_bool = True if terms and terms.lower() in ["yes", "true", "1", "on"] else False

        return JsonResponse({"user_type": user_type, "terms_and_conditions": terms_bool},status=201)

    except Exception as e:
        logger.exception("Error in user_type API")
        return JsonResponse(
            {"error": "Something went wrong", "details": str(e)},
            status=500
        )

@csrf_exempt
@api_view(['POST'])
def user_registration(request):
    try:
        user_type  = request.POST.get("user_registration_type")
        terms      = request.POST.get("terms_and_conditions")
        terms_bool = True if terms and terms.lower() in ["yes", "true", "1", "on"] else False

        if not user_type:
            return JsonResponse({"error": "User type is required."}, status=400)

        if user_type.lower() == "arbitrator":
            arbitrator = Arbitrator.objects.create(
                USER_TYPE                           = user_type,
                FULL_NAME                           = request.POST.get("full_name"),
                DATE_OF_BIRTH                       = request.POST.get("date_of_birth") or None,
                GENDER                              = request.POST.get("gender"),
                NATIONALITY                         = request.POST.get("nationality"),
                PERMANENT_ADDRESS                   = request.POST.get("permanent_address"),
                MOBILE_NO                           = request.POST.get("mobile_no"),
                EMAIL_ID                            = request.POST.get("email_id"),
                AADHAR_NO                           = request.POST.get("aadhar_no"),
                PASSPORT_NO                         = request.POST.get("passport_no"),
                CURRENT_OCCUPATION_DESIGNATION      = request.POST.get("current_occupation_designation"),
                ORGANIZATION_NAME                   = request.POST.get("organization_name"),
                OFFICE_ADDRESS                      = request.POST.get("office_address"),
                PROFESSIONAL_CONTACT_NO             = request.POST.get("professional_contact_no"),
                OFFICIAL_EMAIL_ID                   = request.POST.get("official_email_id"),
                SANAD_ID                            = request.POST.get("sanad_id"),
                WEBSITE                             = request.POST.get("website"),
                QUALIFICATION                       = request.POST.get("qualification"),
                UNIVERSITY_NAME                     = request.POST.get("university_name"),
                YEAR_OF_PASSING                     = request.POST.get("year_of_passing") or None,
                SPECIALIZATION                      = request.POST.get("specialization"),
                MEMBERSHIPS                         = request.POST.get("memberships"),
                NUMBER_OF_ARBITRATIONS_CONDUCTED    = request.POST.get("number_of_arbitrations_conducted") or None,
                SECTORS_OF_EXPERIENCE               = request.POST.get("sectors_of_experience"),
                YEAR_OF_EXPERIENCE                  = request.POST.get("year_of_experience") or None,
                MEDIATION_EXPERIENCE                = request.POST.get("mediation_experience"),
                TRAININGS_CERTIFICATIONS            = request.POST.get("trainings_certifications"),
                AREA_OF_SPECIALIZATION              = request.POST.get("area_of_specialization"),
                LANGUAGES_PROFICIENCY               = request.POST.get("language_proficiency"),
                DECLARATION_AND_DISCLOSURE          = request.POST.get("declaration_and_disclosure_name"),
                DECLARATION_DATE                    = request.POST.get("declaration_date") or None,
                DECLARATION_PLACE                   = request.POST.get("declaration_place"),
                UPDATED_CV                          = request.FILES.get("updated_cv"),
                ID_PROOF_FILE                       = request.FILES.get("id_proof_file"),
                PAN_CARD_FILE                       = request.FILES.get("pan_card_file"),
                PASSPORT_SIZE_PHOTO_FILE            = request.FILES.get("passport_size_photo_file"),
                EDUCATION_CERTIFICATION_FILE        = request.FILES.get("education_certification_file"),
                SANAD_ID_FILE                       = request.FILES.get("sanad_id_file"),
                MEMBERSHIP_CERTIFICATION_FILE       = request.FILES.get("membership_certification_file"),
                TERMS_AND_CONDITIONS                = terms_bool,
            )
            return JsonResponse({"message": "Arbitrator registration successful","type":user_type, "id": arbitrator.id}, status=200)

        elif user_type.lower() == "mediator":
            mediator = Mediator.objects.create(
                USER_TYPE                             = user_type,
                FULL_NAME                             = request.POST.get("full_name"),
                DATE_OF_BIRTH                         = request.POST.get("date_of_birth") or None,
                GENDER                                = request.POST.get("gender"),
                NATIONALITY                           = request.POST.get("nationality"),
                PERMANENT_ADDRESS                     = request.POST.get("permanent_address"),
                MOBILE_NO                             = request.POST.get("mobile_no"),
                EMAIL_ID                              = request.POST.get("email_id"),
                CURRENT_OCCUPATION_DESIGNATION        = request.POST.get("current_occupation_designation"),
                ORGANIZATION_NAME                     = request.POST.get("organization_name"),
                OFFICE_ADDRESS                        = request.POST.get("office_address"),
                PROFESSIONAL_CONTACT_NO               = request.POST.get("professional_contact_no"),
                OFFICIAL_EMAIL_ID                     = request.POST.get("official_email_id"),
                QUALIFICATION                         = request.POST.get("qualification"),
                UNIVERSITY_NAME                       = request.POST.get("university_name"),
                YEAR_OF_PASSING                       = request.POST.get("year_of_passing") or None,
                SPECIALIZATION                        = request.POST.get("specialization"),
                MEMBERSHIPS                           = request.POST.get("memberships"),
                NUMBER_OF_MEDIATION_CONDUCTED         = request.POST.get("number_of_arbitrations_conducted") or None,
                SECTORS_OF_EXPERIENCE                 = request.POST.get("sectors_of_experience"),
                YEAR_OF_EXPERIENCE                    = request.POST.get("year_of_experience") or None,
                MEDIATION_CONCILIATION_EXPERIENCE     = request.POST.get("mediation_conciliation_experience"),
                TRAININGS_CERTIFICATIONS              = request.POST.get("trainings_certifications"),
                AREA_OF_SPECIALIZATION                = request.POST.get("area_of_specialization"),
                LANGUAGES_PROFICIENCY                 = request.POST.get("language_proficiency"),
                DECLARATION_AND_DISCLOSURE_FULL_NAME  = request.POST.get("declaration_and_disclosure_name"),
                DECLARATION_DATE                      = request.POST.get("declaration_date") or None,
                DECLARATION_PLACE                     = request.POST.get("declaration_place"),
                UPDATED_CV                            = request.FILES.get("updated_cv"),
                ID_PROOF_FILE                         = request.FILES.get("id_proof_file"),
                PAN_CARD_FILE                         = request.FILES.get("pan_card_file"),
                PASSPORT_SIZE_PHOTO_FILE              = request.FILES.get("passport_size_photo_file"),
                EDUCATION_CERTIFICATION_FILE          = request.FILES.get("education_certification_file"),
                MEMBERSHIP_CERTIFICATION_FILE         = request.FILES.get("membership_certification_file"),
                TERMS_AND_CONDITIONS=terms_bool,
            )
            return JsonResponse({"message": "Mediator registration successful","type":user_type, "id": mediator.id}, status=200)

        elif user_type.lower() == "bank_individual":
             state_id   = request.POST.get("state")
             city_id    = request.POST.get("city")
             bank_name  = request.POST.get("bank_name")

             state_name = None
             city_name = None

             if state_id:
                    state_obj = StateMaster.objects.filter(id=state_id, IS_DELETED=False).first()
                    state_name = state_obj.NAME if state_obj else None

             if city_id:
                    city_obj = CityMaster.objects.filter(id=city_id, IS_DELETED=False).first()
                    city_name = city_obj.NAME if city_obj else None

             bank_name_instance = BankMaster.objects.get(id=bank_name)

             bank_user = Bank_individual_user.objects.create(
                USER_TYPE               = user_type,
                FULL_NAME               = request.POST.get("full_name"),
                EMAIL_ID                = request.POST.get("email_id"),
                CONTACT_NO              = request.POST.get("contact_no"),
                BANK                    = bank_name_instance,
                NATIONALITY             = request.POST.get("nationality"),
                STATE                   = state_name,
                CITY                    = city_name,
                PIN_CODE                = request.POST.get("pin_code"),
                ADDRESS                 = request.POST.get("address"),
                PERMANENT_ADDRESS       = request.POST.get("permanent_address"),
                TERMS_AND_CONDITIONS    = terms_bool,
            )
             return JsonResponse({"message": "Bank Individual User registration successful","type":user_type, "id": bank_user.id}, status=200)

        else:
            return JsonResponse({"error": "Invalid user type"}, status=400)

    except Exception as e:
        logger.exception("Error in user_registration API")
        return JsonResponse({"error": str(e)}, status=500)
    

def view_registration_details(request, id):
    user_type       = request.GET.get("type")
    arbitrator      = None
    mediator        = None
    bank_individual = None

    if user_type == "arbitrator":
        arbitrator = Arbitrator.objects.filter(id=id, IS_DELETED=False).all()
    elif user_type == "mediator":
        mediator = Mediator.objects.filter(id=id, IS_DELETED=False).all()
    elif user_type == "bank_individual":
       bank_individual = Bank_individual_user.objects.filter(id=id,IS_DELETED=False).all()

    return render(request, "view_details.html", {"arbitrator": arbitrator,"mediator": mediator,"bank_individual":bank_individual,"user_type": user_type})


@api_view(["POST"])
def send_otp(request):
    try:
        mobile_no_email = request.data.get("mobile_no_email")
        user_type       = request.data.get("user_type")
        otp_for         = request.data.get("otp_for")

        if not mobile_no_email:
            return JsonResponse({"message": "Email/Mobile is required"}, status=400)
        if not user_type:
            return JsonResponse({"message": "User Type is required"}, status=400)
        if user_type not in model_map:
            return JsonResponse({"message": "Invalid user type"}, status=400)

        app_label, model_name = model_map[user_type]
        Model = apps.get_model(app_label, model_name)

        email_fields = ["arbitrator", "mediator", "bank_individual", "admin"]

        if user_type in email_fields:
            user = Model.objects.filter(EMAIL_ID__iexact=mobile_no_email, IS_DELETED=False).first()
        else:
            user = Model.objects.filter(MOBILE_NO=mobile_no_email, IS_DELETED=False).first()

        if not user:
            return JsonResponse({"message": "User does not exist"}, status=404)

        msg, otp = OTPManager.send_otp(mobile_no_email, user_type)
        return JsonResponse({"message": msg, "otp": otp}, status=200)

    except Exception as e:
        logger.exception(e)
        return JsonResponse({"message": "Something went wrong"}, status=500)

def get_client_ip(request):
    """Helper to extract client IP address"""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


@api_view(["POST"])
def verify_otp(request):
    try:
        mobile_no_email = request.data.get("mobile_no_email")
        user_type       = request.data.get("user_type")
        otp             = request.data.get("otp")

        if not all([mobile_no_email, user_type, otp]):
            return JsonResponse({"message": "Missing required parameters"}, status=400)

        if user_type not in model_map:
            return JsonResponse({"message": "Invalid user type. Contact Administrator."}, status=412)

        result = OTPManager.validate_otp(mobile_no_email, otp, user_type)
       
        user_obj = result.get("user") 

        ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip_address:
            ip_address = ip_address.split(',')[0].strip()
        else:
            ip_address = request.META.get('REMOTE_ADDR')

        if request.session.session_key is None:
            request.session.create()

        session_id = request.session.session_key

        request.session['is_authenticated'] = True
        request.session['SESSION_ID'] = session_id
        request.session['USER_ID'] = user_obj.id if user_obj else None
        request.session['USER_TYPE'] = user_type

        LoginLogs.objects.create(
            USER_TYPE=user_type,
            USER=mobile_no_email,
            LOGIN_DATETIME=now(),
            LOGIN_SESSION=session_id,
            IP_ADDRESS=ip_address,
            LOGIN_STATUS=True,
        )

        return JsonResponse({"message": "OTP verified successfully!","user_type": user_type,"user_id": user_obj.id if user_obj else None}, status=200)

    except Exception as e:
        logger.exception(f"Error in verify_otp: {e}")
        return JsonResponse({"message": "Something went wrong"}, status=500)

