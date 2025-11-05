from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from bank_user.views import *

urlpatterns = [

    path('bank_user_dashboard',bank_user_dashboard),
    path('bank_user_head',bank_user_head),
    path('bank_user_script',bank_user_script),
    path('bank_user_header',bank_user_header),
    path('my_cases',my_cases),
    path('my_cases_view',my_cases_view),
    path('upload_cases',upload_cases),
    path("create_single_case",create_single_case),
    path("load_cases",load_cases),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)