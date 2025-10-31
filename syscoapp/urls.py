from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from syscoapp.views import *


urlpatterns = [

    path('',login),
    path("add_user",add_user),
    path('user_registration', user_registration),
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

# Mediator ------------------------------------------->

    path('mediator_dashboard',mediator_dashboard),
    path('mediator_head',mediator_head),
    path('mediator_script',mediator_script),
    path('mediator_header',mediator_header),
    path('mediation_cases',mediation_cases),
    path('mediation_cases_view',mediation_cases_view),
    path('sessions',sessions),

# Sysco Admin ------------------------------------------->

    path('sysco_admin_dashboard',sysco_admin_dashboard),
    path('arbitrators',arbitrators),
    path('add_arbitrator',add_arbitrator),
    path('arbitrator_view',arbitrator_view),
    path('cash_queue',cash_queue),
    path('cash_queue_view',cash_queue_view),
    path('upload_cases',upload_cases),
    path('sysco_admin_header',sysco_admin_header),
    path('sysco_admin_head',sysco_admin_head),
    path('sysco_admin_script',sysco_admin_script),
    path('hearings',hearings),
    path('template',template),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

