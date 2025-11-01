from email import header
from django.shortcuts import render
from rest_framework.decorators import api_view 
from django.http import JsonResponse, FileResponse, Http404
from master.models import StateMaster, CityMaster
from user.utils.auth_decorator import custom_authentication
import logging
logger = logging.getLogger()


# Create your views here.
@custom_authentication
def state_master(request):
    return render(request,"state_master.html")

@custom_authentication
@api_view(["POST"])
def add_state(request):
    try:
        state_name = request.data.get("state_name")
        if not state_name:  # Handle empty input
            return JsonResponse({"message": "State Name is required"}, status=400)

        if StateMaster.objects.filter(NAME=state_name, IS_DELETED=False).exists():
            return JsonResponse({"message": "State Name Name already exists"}, status=400)

        StateMaster.objects.create(NAME=state_name)
        return JsonResponse({"message": "State Name Name added successfully"}, status=201)
    except Exception as e:
        logger.exception(e)
        return JsonResponse({"message": f"Something went wrong: {str(e)}"}, status=500)
    

def load_state(request):
    try:
        data = list(StateMaster.objects.filter(IS_DELETED=False).values("id","NAME").order_by("NAME"))
        return JsonResponse({"data":data},safe=False,status=200)
    except Exception as e:
        logger.exception(e)
        return JsonResponse({"message":"Something went Wrong"},safe=False,status=500)
    
@custom_authentication
def get_state(request,id):
    try:
        data = list(StateMaster.objects.filter(id=id).values("id","NAME")   )
        return JsonResponse(data,safe=False,status=200)
    except Exception as e:
        logger.exception(e)
        return JsonResponse({"message":"Something went Wrong"},safe=False,status=500)
    
@custom_authentication
@api_view(['POST'])
def edit_state(request,id):
    try:
        state_name     = request.data.get("state_name")

        if StateMaster.objects.filter(NAME=state_name,IS_DELETED=False).exclude(id=id).exists():
            return JsonResponse({"message": "State Name Already Exist"}, safe=False, status=400)
                    
        edit = StateMaster.objects.get(id=id)
        edit.NAME            = state_name      
        edit.save()
        return JsonResponse({"message":"State Name Edited Successfully"},safe=False,status=200)
    except Exception as e:
        logger.exception(e)
        return JsonResponse({"message":"Something went Wrong"},safe=False,status=500)
    
@custom_authentication  
def city_master(request):
    return render(request,"city_master.html")

@custom_authentication
@api_view(["POST"])
def add_city(request):
    try:
        state_name  = request.data.get("state_name")
        city_name   = request.data.get("city_name")
        
        if not city_name:  # Handle empty input
            return JsonResponse({"message": "City Name is required"}, status=400)

        if CityMaster.objects.filter(STATE=state_name,NAME=city_name, IS_DELETED=False).exists():
            return JsonResponse({"message": "City Name Name already exists"}, status=400)

        CityMaster.objects.create(
            NAME=city_name,
            STATE          = StateMaster.objects.get(id=state_name)
            )
        return JsonResponse({"message": "City Name Name added successfully"}, status=201)
    except Exception as e:
        logger.exception(e)
        return JsonResponse({"message": f"Something went wrong: {str(e)}"}, status=500)

def load_city(request):
    try:
        data = list(CityMaster.objects.filter(IS_DELETED=False).values("id","STATE__NAME","NAME").order_by("-id"))
        return JsonResponse({"data":data},safe=False,status=200)
    except Exception as e:
        logger.exception(e)
        return JsonResponse({"message":"Something went Wrong"},safe=False,status=500)
    
@custom_authentication  
def get_city(request,id):
    try:
        data = list(CityMaster.objects.filter(id=id).values("id","STATE_id","NAME"))
        return JsonResponse(data,safe=False,status=200)
    except Exception as e:
        logger.exception(e)
        return JsonResponse({"message":"Something went Wrong"},safe=False,status=500)

def dropdown_city(request):
    state_id    = request.GET.get("state_id")
    city        = list(CityMaster.objects.filter(STATE__id=state_id).values("id","STATE_id","NAME"))
    # logger.info(f'''
    #     state_id = {state_id}
    #     cityeee = {city}
    # ''')
    return JsonResponse(city,safe=False,status=200)

@custom_authentication
@api_view(['POST'])
def edit_city(request,id):
    try:
        state_name    = request.data.get("state_name")
        city_name     = request.data.get("city_name")

        if CityMaster.objects.filter(STATE=state_name,NAME=city_name,IS_DELETED=False).exclude(id=id).exists():
            return JsonResponse({"message": "City Name Already Exist"}, safe=False, status=400)
                    
        edit = CityMaster.objects.get(id=id)
        edit.STATE          = StateMaster.objects.get(id=state_name)      
        edit.NAME           = city_name      
        edit.save()
        return JsonResponse({"message":"City Name Edited Successfully"},safe=False,status=200)
    except Exception as e:
        logger.exception(e)
        return JsonResponse({"message":"Something went Wrong"},safe=False,status=500)
