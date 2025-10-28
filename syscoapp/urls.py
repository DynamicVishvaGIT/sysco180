from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from syscoapp.views import *


urlpatterns = [
    path('',login),
    path("add_user",add_user),
    path('arbitrator',arbitrator),
    path('mediator',mediator),
    path('personal_information',personal_information),
    path('review',review),

# Arbitrator -------------------------------------------->

    path('arbitrator_dashboard',arbitrator_dashboard),
    path('assigned_cases',assigned_cases),
    path('assigned_cases_view',assigned_cases_view),
    path('arbitrator_head',arbitrator_head),
    path('arbitrator_header',arbitrator_header),
    path('arbitrator_script',arbitrator_script),

# Bank User ------------------------------------------->

    path('bank_user_dashboard',bank_user_dashboard),
    path('bank_user_head',bank_user_head),
    path('bank_user_script',bank_user_script),
    path('bank_user_header',bank_user_header),
    path('my_cases',my_cases),
    path('my_cases_view',my_cases_view),
    path('upload_cases',upload_cases),













]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

