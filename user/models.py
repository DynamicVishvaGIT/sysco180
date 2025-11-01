from django.db import models
from datetime import date

# Create your models here.

class SoftDeleteTimestampMixin(models.Model):
    IS_DELETED      = models.BooleanField(default=False, db_index=True) 
    CREATED_DATE    = models.DateTimeField(auto_now_add=True,null=True)
    UPDATED_DATE    = models.DateTimeField(auto_now=True,null=True)

    def delete(self, *args, **kwargs):
        """Soft delete the record instead of removing it."""
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True

class Arbitrator(SoftDeleteTimestampMixin,models.Model):
    USER_TYPE                         = models.CharField(max_length=50, blank=True, null=True)
    FULL_NAME                         = models.CharField(max_length=200, blank=True, null=True)
    DATE_OF_BIRTH                     = models.DateField(blank=True, null=True)
    GENDER                            = models.CharField(max_length=255, blank=True, null=True)
    NATIONALITY                       = models.CharField(max_length=50, blank=True, null=True)
    PERMANENT_ADDRESS                 = models.TextField(blank=True, null=True)
    MOBILE_NO                         = models.CharField(max_length=15, blank=True, null=True)
    EMAIL_ID                          = models.EmailField(max_length=254, blank=True, null=True)
    AADHAR_NO                         = models.CharField(max_length=12, blank=True, null=True)
    PASSPORT_NO                       = models.CharField(max_length=20, blank=True, null=True)
    CURRENT_OCCUPATION_DESIGNATION    = models.CharField(max_length=200, blank=True, null=True)
    ORGANIZATION_NAME                 = models.CharField(max_length=200, blank=True, null=True)
    OFFICE_ADDRESS                    = models.TextField(blank=True, null=True)
    PROFESSIONAL_CONTACT_NO           = models.CharField(max_length=15, blank=True, null=True)
    OFFICIAL_EMAIL_ID                 = models.EmailField(max_length=254, blank=True, null=True)
    SANAD_ID                          = models.CharField(max_length=50, blank=True, null=True)
    WEBSITE                           = models.URLField(blank=True, null=True)
    QUALIFICATION                     = models.CharField(max_length=200, blank=True, null=True)
    UNIVERSITY_NAME                   = models.CharField(max_length=200, blank=True, null=True)
    YEAR_OF_PASSING                   = models.PositiveIntegerField(blank=True, null=True)
    SPECIALIZATION                    = models.CharField(max_length=200, blank=True, null=True)
    MEMBERSHIPS                       = models.CharField(max_length=500, blank=True, null=True)
    NUMBER_OF_ARBITRATIONS_CONDUCTED  = models.PositiveIntegerField(blank=True, null=True)
    SECTORS_OF_EXPERIENCE             = models.CharField(max_length=300, blank=True, null=True)
    YEAR_OF_EXPERIENCE                = models.PositiveIntegerField(blank=True, null=True)
    MEDIATION_EXPERIENCE              = models.CharField(max_length=300, blank=True, null=True)
    TRAININGS_CERTIFICATIONS          = models.CharField(max_length=500, blank=True, null=True)
    AREA_OF_SPECIALIZATION            = models.CharField(max_length=500, blank=True, null=True)
    LANGUAGES_PROFICIENCY             = models.CharField(max_length=300, blank=True, null=True)
    DECLARATION_AND_DISCLOSURE        = models.CharField(max_length=200, blank=True, null=True)
    DECLARATION_DATE                  = models.DateField(blank=True, null=True)
    DECLARATION_PLACE                 = models.CharField(max_length=100, blank=True, null=True)
    UPDATED_CV                        = models.FileField(upload_to='arbitrators_cv/', blank=True, null=True)
    ID_PROOF_FILE                     = models.FileField(upload_to='arbitrators_id_proof/', blank=True, null=True)
    PAN_CARD_FILE                     = models.FileField(upload_to='arbitrators_pan/', blank=True, null=True)
    PASSPORT_SIZE_PHOTO_FILE          = models.FileField(upload_to='arbitrators_photo/', blank=True, null=True)
    EDUCATION_CERTIFICATION_FILE      = models.FileField(upload_to='arbitrators_education/', blank=True, null=True)
    SANAD_ID_FILE                     = models.FileField(upload_to='arbitrators_sanad/', blank=True, null=True)
    MEMBERSHIP_CERTIFICATION_FILE     = models.FileField(upload_to='arbitrators_membership/', blank=True, null=True)

    TERMS_AND_CONDITIONS              = models.BooleanField(default=False,blank=True,null=True)

    class Meta:
        verbose_name_plural = "Arbitrators"

class Mediator(SoftDeleteTimestampMixin, models.Model):
    USER_TYPE                              = models.CharField(max_length=50, blank=True, null=True)
    FULL_NAME                              = models.CharField(max_length=200, blank=True, null=True)
    DATE_OF_BIRTH                          = models.DateField(blank=True, null=True)
    GENDER                                 = models.CharField(max_length=255, blank=True, null=True)
    NATIONALITY                            = models.CharField(max_length=50, blank=True, null=True)
    PERMANENT_ADDRESS                      = models.TextField(blank=True, null=True)
    MOBILE_NO                              = models.CharField(max_length=15, blank=True, null=True)
    EMAIL_ID                               = models.EmailField(max_length=254, blank=True, null=True)

    CURRENT_OCCUPATION_DESIGNATION         = models.CharField(max_length=200, blank=True, null=True)
    ORGANIZATION_NAME                      = models.CharField(max_length=200, blank=True, null=True)
    OFFICE_ADDRESS                         = models.TextField(blank=True, null=True)
    PROFESSIONAL_CONTACT_NO                = models.CharField(max_length=15, blank=True, null=True)
    OFFICIAL_EMAIL_ID                      = models.EmailField(max_length=254, blank=True, null=True)

    QUALIFICATION                          = models.CharField(max_length=200, blank=True, null=True)
    UNIVERSITY_NAME                        = models.CharField(max_length=200, blank=True, null=True)
    YEAR_OF_PASSING                        = models.PositiveIntegerField(blank=True, null=True)
    SPECIALIZATION                         = models.CharField(max_length=200, blank=True, null=True)

    MEMBERSHIPS                            = models.CharField(max_length=500, blank=True, null=True)

    NUMBER_OF_MEDIATION_CONDUCTED          = models.PositiveIntegerField(blank=True, null=True)
    SECTORS_OF_EXPERIENCE                  = models.CharField(max_length=300, blank=True, null=True)
    YEAR_OF_EXPERIENCE                     = models.PositiveIntegerField(blank=True, null=True)
    MEDIATION_CONCILIATION_EXPERIENCE      = models.CharField(max_length=300, blank=True, null=True)

    TRAININGS_CERTIFICATIONS               = models.CharField(max_length=500, blank=True, null=True)

    AREA_OF_SPECIALIZATION                 = models.CharField(max_length=500, blank=True, null=True)

    LANGUAGES_PROFICIENCY                  = models.CharField(max_length=300, blank=True, null=True)

    DECLARATION_AND_DISCLOSURE_FULL_NAME   = models.CharField(max_length=200, blank=True, null=True)
    DECLARATION_DATE                       = models.DateField(blank=True, null=True)
    DECLARATION_PLACE                      = models.CharField(max_length=100, blank=True, null=True)
    UPDATED_CV                             = models.FileField(upload_to='mediator_cv/', blank=True, null=True)
    ID_PROOF_FILE                          = models.FileField(upload_to='mediators_id_proof/', blank=True, null=True)
    PAN_CARD_FILE                          = models.FileField(upload_to='mediator_pan/', blank=True, null=True)
    PASSPORT_SIZE_PHOTO_FILE               = models.FileField(upload_to='mediator_photo/', blank=True, null=True)
    EDUCATION_CERTIFICATION_FILE           = models.FileField(upload_to='mediator_education/', blank=True, null=True)
    MEMBERSHIP_CERTIFICATION_FILE          = models.FileField(upload_to='mediator_membership/', blank=True, null=True)

    TERMS_AND_CONDITIONS                   = models.BooleanField(default=False,blank=True,null=True)
    class Meta:
        verbose_name_plural = "Mediators"

class Bank_individual_user(SoftDeleteTimestampMixin,models.Model):
    USER_TYPE         = models.CharField(max_length=50, blank=True, null=True)
    FULL_NAME         = models.CharField(max_length=200, blank=True, null=True)
    EMAIL_ID          = models.EmailField(max_length=254, blank=True, null=True)
    CONTACT_NO        = models.CharField(max_length=15, blank=True, null=True)
    NATIONALITY       = models.CharField(max_length=50, blank=True, null=True)
    STATE             = models.CharField(max_length=100, blank=True, null=True)
    CITY              = models.CharField(max_length=100, blank=True, null=True)
    PIN_CODE          = models.CharField(max_length=10, blank=True, null=True)
    ADDRESS           = models.TextField(blank=True, null=True)
    PERMANENT_ADDRESS = models.TextField(blank=True, null=True)

    TERMS_AND_CONDITIONS = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Bank Individual Users"


user_choice = [
    ('admin', 'Admin'),
    ('arbitrator', 'Arbitrator'),
    ('mediator', 'Mediator'),
    ('bank_individual', 'Bank_individual'),
]

class LoginLogs(models.Model):
   
    USER_TYPE           = models.CharField(max_length=255, blank=True, choices=user_choice, null=True)
    USER                = models.CharField(max_length=16,blank=True,null=True)
    LOGIN_DATETIME      = models.DateTimeField(null=True,blank=True)
    LOGOUT_DATETIME     = models.DateTimeField(null=True,blank=True)
    LOGIN_SESSION       = models.TextField(blank=True,null=True)
    IP_ADDRESS          = models.CharField(max_length=16,blank=True,null=True)
    LOGIN_STATUS        = models.BooleanField(default=True)
    FCM_TOKEN           = models.CharField(max_length=500,blank=True,null=True)

    class Meta:
        verbose_name_plural = "Login Logs"

class Otp(SoftDeleteTimestampMixin, models.Model):
   
    USER_TYPE           = models.CharField(max_length=255, blank=True, choices=user_choice, null=True)
    EMAIL_ID            = models.CharField(max_length=500,blank=True,null=True)
    PHONE_NUMBER        = models.CharField(max_length=500,blank=True,null=True)
    OTP                 = models.CharField(max_length=10)

    class Meta:
        verbose_name = "OTP"
        verbose_name_plural = "OTP"




