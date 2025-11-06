from functools import wraps
from django.http import JsonResponse
from django.shortcuts import render ,redirect
# Import your User model
from user.models import LoginLogs

#logger
import logging
logger = logging.getLogger(__name__)

def custom_authentication(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        try:
            # Extract headers
            device_type = request.headers.get("device-type")

            logger.info(f"device_type = {device_type}")
        
            if device_type == "mobile":
                auth_token  = request.headers.get("Authorization") or request.META.get("HTTP_AUTHORIZATION")

                if not auth_token:
                    return JsonResponse({"message": "Authentication credentials were not provided."}, status=401)

                # Fetch latest login session based on token
                login = LoginLogs.objects.filter(LOGIN_SESSION=auth_token).last()
                if not login:
                    return JsonResponse({"message": "Invalid token."}, status=401)

                # Check if token has expired
                if login.LOGOUT_DATETIME:
                    return JsonResponse({"message": "Token has expired."}, status=401)

                # Attach relevant user and society/flat details to request
                request.device_type = "mobile"
                request.login_id    = login.USER
                request.user_type   = login.USER_TYPE

            else:
                if 'is_authenticated' in request.session:
                    request.device_type = "web"
                    request.login_id    = request.session['USER_ID']
                    request.user_type   = request.session['USER_TYPE']
                else:
                    return redirect("/")
            return view_func(request, *args, **kwargs)

        except Exception as e:
            logger.exception("Error in authentication middleware: %s", str(e))
            return JsonResponse({"message": "Something went wrong."}, safe=False, status=500)

    return wrapped_view