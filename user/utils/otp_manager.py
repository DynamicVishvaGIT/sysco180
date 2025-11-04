import logging
import random
import os
import requests
from django.core.mail import send_mail
from django.conf import settings
from user.models import Otp

logger = logging.getLogger(__name__)


class OTPManager:
    """Handles OTP generation, sending, and validation."""

    @staticmethod
    def generate_otp():
        """Generate a unique 4-digit OTP that does not already exist."""
        while True:
            otp = random.randint(1111, 9999)
            if not Otp.objects.filter(OTP=otp).exists():
                return otp

    @staticmethod
    def send_otp(mobile_no_email, user_type):
        """
        Create and send an OTP (testing mode: returns the OTP directly).

        Args:
            mobile_no_email (str): Email or phone number depending on user type.
            user_type (str): Type of user (admin, retailer, etc.).

        Returns:
            tuple: (message, otp)
        """
        try:
            otp = OTPManager.generate_otp()

            # Create OTP record
            otp_instance = Otp.objects.create(
                OTP=otp,
                USER_TYPE=user_type
            )

            # Assign email or phone field
            if user_type in ["admin", "arbitrator", "mediator", "bank_individual"]:
                otp_instance.EMAIL_ID = mobile_no_email
            else:
                otp_instance.PHONE_NUMBER = mobile_no_email

            otp_instance.save()

            # 🚀 For testing: Return OTP directly instead of sending SMS or Email
            message = f"OTP sent successfully. Your OTP is {otp}"
            logger.info(f"Generated OTP for {mobile_no_email} ({user_type}) = {otp}")

            # You can later integrate real SMS/email sending here
            # Example: send_mail('Your OTP', f'Your OTP is {otp}', settings.DEFAULT_FROM_EMAIL, [mobile_no_email])

            return message, otp

        except Exception as e:
            logger.exception(f"Error generating or sending OTP: {e}")
            return "Error sending OTP", None

    @staticmethod
    def validate_otp(mobile_no_email, otp, user_type):
        """
        Validate OTP for a given mobile number or email.

        Args:
            mobile_no_email (str): Email or phone number.
            otp (str): The OTP entered by the user.
            user_type (str): Type of user.

        Returns:
            dict: {"status": bool, "message": str}
        """
        try:
            # Build filter dynamically based on user type
            filter_kwargs = {"USER_TYPE": user_type}
            if user_type in ["admin", "arbitrator", "mediator", "bank_individual"]:
                filter_kwargs["EMAIL_ID"] = mobile_no_email
            else:
                filter_kwargs["PHONE_NUMBER"] = mobile_no_email

            # Get latest OTP for this user
            otp_record = Otp.objects.filter(**filter_kwargs).order_by("-id").first()

            if not otp_record:
                return {"status": False, "message": "OTP not found or expired"}

            if str(otp_record.OTP) != str(otp):
                return {"status": False, "message": "Invalid OTP"}

            # ✅ OTP matches — delete it to prevent reuse
            otp_record.delete()
            logger.info(f"OTP verified successfully for {mobile_no_email} ({user_type})")

            return {"status": True, "message": "OTP verified successfully"}

        except Exception as e:
            logger.exception(f"Error validating OTP: {e}")
            return {"status": False, "message": "Internal error validating OTP"}
