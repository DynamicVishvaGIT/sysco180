from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user.views import *


urlpatterns = [

    path('',login),
    path("registration",registration),
    path("user_type",user_type),
    path('user_registration', user_registration),
    path('arbitrator',arbitrator),
    path('mediator',mediator),
    path('personal_information',personal_information),
    path('view_details_page',view_details_page),
    path('view_registration_details/<int:id>', view_registration_details),

    path('send_otp',send_otp),
    path('verify_otp',verify_otp),

# Arbitrator -------------------------------------------->

    path('arbitrator_dashboard',arbitrator_dashboard),
    path('assigned_cases',assigned_cases),
    path('assigned_cases_view',assigned_cases_view),
    path('arbitrator_head',arbitrator_head),
    path('arbitrator_header',arbitrator_header),
    path('arbitrator_script',arbitrator_script),

# Bank User ------------------------------------------->

 
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
    # path('upload_cases',upload_cases),
    path('sysco_admin_header',sysco_admin_header),
    path('sysco_admin_head',sysco_admin_head),
    path('sysco_admin_script',sysco_admin_script),
    path('hearings',hearings),
    path('template',template),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

