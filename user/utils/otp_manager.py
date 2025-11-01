#logger
import logging
logger = logging.getLogger(__name__)

'''This is a import User Models'''
from user.models import Otp
import os
import requests
from django.core.mail import send_mail
from django.conf import settings


class OTPManager:
    @staticmethod
    def generate_otp():
    # while True:
    #     otp = random.randint(1111, 9999)  # Generate a 4-digit OTP
    #     if not Otp.objects.filter(OTP=otp).exists():  # Check uniqueness
    #         return otp      
        return "1234"

    @staticmethod
    def send_otp(mobile_no_email,user_type,owner_name):
        otp = OTPManager.generate_otp()
        otp_instance = Otp.objects.create(
            OTP             = otp,
            USER_TYPE       = user_type 
        )
        if user_type in ["admin","sales_person"]:
            otp_instance.EMAIL_ID = mobile_no_email
            SmsTemplate.send_otp_email(mobile_no_email,user_type,otp,owner_name)
        else:
            otp_instance.PHONE_NUMBER = mobile_no_email
            SmsTemplate.send_sms(mobile_no_email,user_type,otp)
        otp_instance.save()
        return "OTP sent successfully"

    @staticmethod
    def validate_otp(mobile_no_email,otp,user_type):
        """
        Validate OTP for a given mobile number.
        - Returns: Success message or error message.
        """
        filter = {}
        if user_type in ["admin","sales_person"]:
            filter["EMAIL_ID"] = mobile_no_email
        else:
            filter["PHONE_NUMBER"] = mobile_no_email
        otp_record = Otp.objects.filter(**filter,USER_TYPE=user_type).order_by("-id").first()
        # if not otp_record:
        #     return {"status": False, "message": "OTP not found"}
        # if otp_record.OTP != otp:
        #     return {"status": False, "message": "Invalid OTP"}
        if not otp_record or otp_record.OTP != otp:
            return {"status": False, "message": "Invalid OTP"}
        #Delete OTP after successful verification
        # Otp.objects.filter(id=otp_record.id).delete()
        return {"status": True, "message": "OTP verified successfully"}
    
class SmsTemplate:
    @staticmethod
    def send_sms(mobile_no_email,user_type,otp):
        if not user_type in ["admin","sales_person"]:
            url = f"""{os.environ["SMS_URL"]}?username={os.environ["SMS_USERNAME"]}&pass={os.environ["SMS_PASSWORD"]}&senderid={os.environ["SENDER_ID"]}&dest_mobileno=${mobile_no_email}&message=Your OTP for ElMeasure is {otp}. Do not share this with anyone. Valid for 10 minutes. Elmeasure&dltentityid={os.environ["DLTENTITYID"]}&dlttempid={os.environ["DLTTEMPID1"]}&tmid={os.environ["TMID"]}&dltheaderid={os.environ["DLTHEADERID"]}&response=Y"""

            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            return response
        return
    
    def get_clean_email_password():
        """Clean EMAIL_HOST_PASSWORD to remove unwanted characters like \\xa0"""
        try:
            return os.environ["EMAIL_HOST_PASSWORD"].replace('\xa0', ' ').strip()
        except Exception as e:
            logger.warning(f"Failed to clean email password: {e}")
            return os.environ["EMAIL_HOST_PASSWORD"]
    
    def send_otp_email(mobile_no_email, user_type, otp,owner_name):
        # subject = "Your OTP for Verification"
        # message = f"Hello {mobile_no_email},\n\nYour OTP is: {otp}\nIt will expire in 10 minutes."
        subject = "Your OTP for Password Reset"
        message = (
            f"Dear {owner_name},\n\n"
            f"You requested to reset your password for the El-measure Sales App.\n"
            f"Your OTP is: {otp}\n"
            f"This OTP will expire in 10 minutes.\n\n"
            f"If you did not request this, please contact our support team.\n\n"
            f"Best regards,\nTeam El-measure"
        )
        try:
            send_mail(
                subject,
                message,
                os.environ["DEFAULT_FROM_EMAIL"],  # sender
                [mobile_no_email],          # recipient
                fail_silently=False,
                auth_user=os.environ["EMAIL_HOST_USER"],
                auth_password=SmsTemplate.get_clean_email_password(),
            )
            logger.info(f"OTP email sent successfully to {mobile_no_email}")
        except Exception as e:
            logger.error(f"Failed to send OTP email to {mobile_no_email}: {e}")
        return


    def send_account_creation_email(mobile_no_email, owner_name,user_password):
        subject = "El-measure Sales Account Created Successfully"
        message = (
            f"Dear {owner_name},\n\n"
            f"Your account has been created successfully.\n\n"
            f"Here are your login credentials:\n"
            f"Username: {mobile_no_email}\n"
            f"Password: {user_password}\n\n"
            f"You can now log in using your registered credentials.\n\n"
            f"Welcome to El-measure!\n"
            f"We’re glad to have you on board.\n\n"
            f"Best regards,\nTeam El-measure"
        )
        try:
            send_mail(
                subject,
                message,
                os.environ["DEFAULT_FROM_EMAIL"],  # sender
                [mobile_no_email],
                fail_silently=False,
                auth_user=os.environ["EMAIL_HOST_USER"],
                auth_password=SmsTemplate.get_clean_email_password(),
            )
            logger.info(f"Account creation email sent successfully to {mobile_no_email}")
        except Exception as e:
            logger.error(f"Failed to send account creation email to {mobile_no_email}: {e}")
        return
    
    # def send_otp_email(mobile_no_email,user_type,otp):
    #     subject = "Your OTP for Verification"
    #     message = f"Hello {mobile_no_email},\n\nYour OTP is: {otp}\nIt will expire in 10 minutes"
    #     send_mail(subject, message, None, [mobile_no_email])
    #     return

    # def send_account_creation_email(mobile_no_email,owner_name):
    #     subject = "El-measure Sales Account Created Successfully"
    #     message = f"Dear {owner_name},\n\n Your account has been created successfully.\nYou can now log in using your registered credentials.\n\n Welcome to El-measure!\n We’re glad to have you on board\n\nBest regards,\nTeam El-measure"
    #     send_mail(subject, message, None, [mobile_no_email])
    #     return
    
    def send_login_success_sms(mobile_no_email,user_type):
        if not user_type in ["admin","sales_person"]:
            url = f"""{os.environ["SMS_URL"]}?username={os.environ["SMS_USERNAME"]}&pass={os.environ["SMS_PASSWORD"]}&senderid={os.environ["SENDER_ID"]}&dest_mobileno=${mobile_no_email}&message=Your ElMeasure account has been approved. You can now log in using your registered credentials. Welcome aboard!&dltentityid={os.environ["DLTENTITYID"]}&dlttempid={os.environ["DLTTEMPID2"]}&tmid={os.environ["TMID"]}&dltheaderid={os.environ["DLTHEADERID"]}&response=Y"""

            # logger.info(f"url = {url}")
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            return response
        return

