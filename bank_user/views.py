from email import header
from django.shortcuts import render
from rest_framework.decorators import api_view 
from django.http import JsonResponse, FileResponse, Http404
from bank_user.models import *
import os
import pandas as pd
from django.db import transaction

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
    

@api_view(["POST"])
# @custom_authentication
def upload_bulk_cases(request):
    try:
        login_id     = 4
        excel_file   = request.FILES.get("bulk_cases_excel_sheet")

        logger.info(f''' 
            login_id   = {login_id}
            excel_file = {excel_file}
 ''')

        if not excel_file:
            return JsonResponse({"message": "Excel file is required"}, status=400)

        ext = os.path.splitext(excel_file.name)[1].lower()
        if ext not in [".xls", ".xlsx"]:
            return JsonResponse({"message": "Upload only .xls or .xlsx format"}, status=412)

        df = pd.read_excel(excel_file, dtype=str).fillna("")
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        required = [
            'intent_ref_no', 'email_id', 'loan_agreement_no', 'customer_name',
            'customer_address', 'advocate_name', 'arbitrator_name', 'arbitrator_address',
            'lrn_date', 'lrn_ref_no', 'loan_amount', 'loan_agreement_date',
            'pending_due_amount', 'total_outstanding_amount', 'outstanding_amount_on_date',
            'product_name'
        ]

        missing = [c for c in required if c not in df.columns]
        if missing:
            return JsonResponse({"message": f"Missing columns in Excel: {missing}"}, status=400)

        bank_cases = BankCases.objects.create(BANK_USER_id=login_id)

        with transaction.atomic():
            for idx, row in df.iterrows():

                case_obj = Cases.objects.create(
                    BANK_CASES=bank_cases,
                    INTENT_REFERENCE_NO=row['intent_ref_no'],
                    EMAIL_ID=row['email_id'],
                    LOAN_AGREEMENT_NO=row['loan_agreement_no'],
                    CUSTOMER_NAME=row['customer_name'],
                    CUSTOMER_ADDRESS=row['customer_address'],
                    ADVOCATE_NAME=row['advocate_name'],
                    ARBITRATOR_NAME=row['arbitrator_name'],
                    ARBITRATOR_ADDRESS=row['arbitrator_address'],
                    LRN_DATE=pd.to_datetime(row['lrn_date']).date() if row['lrn_date'] else None,
                    LRN_REFERENCE_NO=row['lrn_ref_no'],
                    LOAN_AMOUNT=row['loan_amount'] or None,
                    LOAN_AGREEMENT_DATE=pd.to_datetime(row['loan_agreement_date']).date() if row['loan_agreement_date'] else None,
                    PENDING_DUE_AMOUNT=row['pending_due_amount'] or None,
                    TOTAL_OUTSTANDING_AMOUNT=row['total_outstanding_amount'] or None,
                    OUTSTANDING_AMOUNT_ON_DATE=pd.to_datetime(row['outstanding_amount_on_date']).date() if row['outstanding_amount_on_date'] else None,
                    PRODUCT_NAME=row['product_name']
                )

                for col in df.columns:
                    if col.startswith("party_name_"):
                        index = col.split("_")[-1] 
                        p_name = row[col].strip()
                        p_address_col = f"party_address_{index}"
                        p_address = row.get(p_address_col, "").strip()

                        if p_name:
                            CasePartyDetails.objects.create(
                                BULK_UPLOAD_CASE=case_obj,
                                PARTY_NAME=p_name,
                                PARTY_ADDRESS=p_address
                            )

        return JsonResponse({"message": "Bulk Case Upload Successful"}, status=201)

    except Exception as e:
        return JsonResponse({"message": f"Something went wrong: {str(e)}"}, status=500)





