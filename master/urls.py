from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from master.views import *

urlpatterns = [
    path('state_master',state_master),
    path('add_state',add_state),
    path('load_state',load_state),
    path('get_state/<id>',get_state),
    path('edit_state/<id>',edit_state),

    path('city_master',city_master),
    path('add_city',add_city),
    path('load_city',load_city),
    path('get_city/<id>',get_city),
    path('dropdown_city',dropdown_city),
    path('edit_city/<id>',edit_city),
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)