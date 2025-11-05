from email import header
from django.shortcuts import render
from rest_framework.decorators import api_view 
from django.http import JsonResponse, FileResponse, Http404
from bank_user.models import *
from user.utils.auth_decorator import custom_authentication
from django.db.models import Prefetch
import logging
logger = logging.getLogger()

def bank_user_head(request):
    return render(request,'bank_user/head.html')

def bank_user_script(request):
    return render(request,'bank_user/script.html')

def bank_user_header(request):
    return render(request,'bank_user/header.html')

def bank_user_dashboard(request):
    return render(request,'bank_user/bank_user_dashboard.html')

def my_cases(request):
    return render(request,'bank_user/my_cases.html')

def my_cases_view(request):
    return render(request,'bank_user/my_cases_view.html')

def upload_cases(request):
    return render(request,'bank_user/upload_cases.html')

@api_view(['POST'])
def create_single_case(request):
    try:
        intent_reference_no   = request.POST.get('intent_reference_no')
        email_id              = request.POST.get('email_id')
        loan_agreement_no     = request.POST.get('loan_agreement_no')
        customer_name         = request.POST.get('customer_name')
        customer_address      = request.POST.get('customer_address')
        advocate_name         = request.POST.get('advocate_name')
        arbitrator_name       = request.POST.get('arbitrator_name')
        arbitrator_address    = request.POST.get('arbitrator_address')
        lrn_date              = request.POST.get('lrn_date')
        lrn_ref_no            = request.POST.get('lrn_ref_no')
        loan_amount           = request.POST.get('loan_amount')
        loan_agreement_date   = request.POST.get('loan_agreement_date')

        party_name             = request.POST.getlist('party_name')
        party_address          = request.POST.getlist('party_address')
        pending_due_amt        = request.POST.getlist('pending_due_amt')
        total_outstanding_amt  = request.POST.getlist('total_outstanding_amt')
        outstanding_amt_date   = request.POST.getlist('outstanding_amt_date')
        product_name           = request.POST.getlist('product_name')

        logger.info(f''' 
                    
        intent_reference_no    = {intent_reference_no}
        email_id               = {email_id}
        loan_agreement_no      = {loan_agreement_no}
        customer_name          = {customer_name}
        customer_address       = {customer_address}
        advocate_name          = {advocate_name}
        arbitrator_name        = {arbitrator_name}       
        arbitrator_address     = {arbitrator_address}
        lrn_date               = {lrn_date}
        lrn_ref_no             = {lrn_ref_no}
        loan_amount            = {loan_amount}
        loan_agreement_date    = {loan_agreement_date}

        party_name             = {party_name}
        party_address          = {party_address}
        pending_due_amt        = {pending_due_amt}
        total_outstanding_amt  = {total_outstanding_amt}
        outstanding_amt_date   = {outstanding_amt_date}      
        product_name           = {product_name}
       
''')
        case = Case.objects.create(
            INTENT_REFERENCE_NO = intent_reference_no,
            EMAIL_ID            = email_id,
            LOAN_AGREEMENT_NO   = loan_agreement_no,
            CUSTOMER_NAME       = customer_name,
            CUSTOMER_ADDRESS    = customer_address,
            ADVOCATE_NAME       = advocate_name,
            ARBITRATOR_NAME     = arbitrator_name,
            ARBITRATOR_ADDRESS  = arbitrator_address,
            LRN_DATE            = lrn_date or None,
            LRN_REFERENCE_NO    = lrn_ref_no,
            LOAN_AMOUNT         = loan_amount or None,
            LOAN_AGREEMENT_DATE = loan_agreement_date or None,
        )

        num_entries = len(party_name)
        for i in range(num_entries):
            CasePartyDetails.objects.create(
                CASE                       = case,
                PARTY_NAME                 = party_name[i] if i < len(party_name) else None,
                PARTY_ADDRESS              = party_address[i] if i < len(party_address) else None,
                PENDING_DUE_AMOUNT         = pending_due_amt[i] if i < len(pending_due_amt) and pending_due_amt[i] != "" else None,
                TOTAL_OUTSTANDING_AMOUNT   = total_outstanding_amt[i] if i < len(total_outstanding_amt) and total_outstanding_amt[i] != "" else None,
                OUTSTANDING_AMOUNT_ON_DATE = outstanding_amt_date[i] if i < len(outstanding_amt_date) and outstanding_amt_date[i] != "" else None,
                PRODUCT_NAME               = product_name[i] if i < len(product_name) else None,
            )

        return JsonResponse({"message": "Case created successfully","case_id": case.id}, status=200)

    except Exception as e:
        logger.exception("Error in create_single_case: %s", str(e))
        return JsonResponse({"message": "Something went wrong","error": str(e)}, status=500)


def load_cases(request):
    try:
        cases = Case.objects.filter(IS_DELETED=False).prefetch_related(Prefetch('details',queryset=CasePartyDetails.objects.filter(IS_DELETED=False)))

        data = []
        for case in cases:
            party_names = [d.PARTY_NAME for d in case.details.all() if d.PARTY_NAME]

            data.append({
                "id": case.id,
                "CUSTOMER_NAME": case.CUSTOMER_NAME,
                "EMAIL_ID": case.EMAIL_ID,
                "PARTY_NAMES": party_names,
                "UPLOAD_DATE": case.CREATED_DATE.strftime("%d-%m-%Y") if case.CREATED_DATE else "",
                "ADVOCATE_NAME": case.ADVOCATE_NAME ,
                "ARBITRATOR_NAME": case.ARBITRATOR_NAME ,
            })

        return JsonResponse({"data": data}, status=200)

    except Exception as e:
        print(e)
        return JsonResponse({"error": "Something went wrong"}, status=500)



