from django.shortcuts import render

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

