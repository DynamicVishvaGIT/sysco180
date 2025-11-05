from django.db import models
from user.models import *

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


class Case(SoftDeleteTimestampMixin, models.Model):

    INTENT_REFERENCE_NO    = models.CharField(max_length=50, blank=True, null=True, verbose_name="Intent Reference Number")
    EMAIL_ID               = models.EmailField(max_length=254, blank=True, null=True, verbose_name="Email ID")
    LOAN_AGREEMENT_NO      = models.CharField(max_length=100, blank=True, null=True, verbose_name="Loan Agreement / Prospect Number")
    CUSTOMER_NAME          = models.CharField(max_length=200, blank=True, null=True, verbose_name="Customer Name")
    CUSTOMER_ADDRESS       = models.TextField(blank=True, null=True, verbose_name="Customer Address")
    ADVOCATE_NAME          = models.CharField(max_length=200, blank=True, null=True, verbose_name="Advocate Name")
    ARBITRATOR_NAME        = models.CharField(max_length=200, blank=True, null=True, verbose_name="Arbitrator Name")
    ARBITRATOR_ADDRESS     = models.TextField(blank=True, null=True, verbose_name="Arbitrator Address")
    LRN_DATE               = models.DateField(blank=True, null=True, verbose_name="LRN Date")
    LRN_REFERENCE_NO       = models.CharField(max_length=100, blank=True, null=True, verbose_name="LRN Reference Number")
    LOAN_AMOUNT            = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Loan Amount (₹)")
    LOAN_AGREEMENT_DATE    = models.DateField(blank=True, null=True, verbose_name="Loan Agreement Date")

    class Meta:
        verbose_name = "Case"
        verbose_name_plural = "Cases"

class CasePartyDetails(SoftDeleteTimestampMixin, models.Model):
    CASE                       = models.ForeignKey("bank_user.Case", on_delete=models.CASCADE,null=True,blank=True, related_name="details" )
    PARTY_NAME                 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Party Name")
    PARTY_ADDRESS              = models.TextField(blank=True, null=True, verbose_name="Party Address")
    PENDING_DUE_AMOUNT         = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Pending Due Amount (₹)")
    TOTAL_OUTSTANDING_AMOUNT   = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Total Outstanding Amount (₹)")
    OUTSTANDING_AMOUNT_ON_DATE = models.DateField(blank=True, null=True, verbose_name="Outstanding Amount on Date")
    PRODUCT_NAME               = models.CharField(max_length=200, blank=True, null=True, verbose_name="Product Name")
    
    class Meta:
        verbose_name = "Case Party Details"
        verbose_name_plural = "Case Party Details"


# class Bank(SoftDeleteTimestampMixin, models.Model):

#     BANK_NAME    = models.CharField(max_length=225, blank=True, null=True, verbose_name="Bank Name")

#     class Meta:
#         verbose_name = "Bank"
#         verbose_name_plural = "Bank"

class Bulk_Upload_Cases(SoftDeleteTimestampMixin, models.Model):

    BANK_USER              = models.ForeignKey("user.Bank_individual_user", on_delete=models.CASCADE,null=True,blank=True)
    INTENT_REFERENCE_NO    = models.CharField(max_length=100, blank=True, null=True, verbose_name="Intent Reference Number")
    EMAIL_ID               = models.EmailField(max_length=254, blank=True, null=True, verbose_name="Email ID")
    LOAN_AGREEMENT_NO      = models.CharField(max_length=100, blank=True, null=True, verbose_name="Loan Agreement / Prospect Number")
    CUSTOMER_NAME          = models.CharField(max_length=200, blank=True, null=True, verbose_name="Customer Name")
    CUSTOMER_ADDRESS       = models.TextField(blank=True, null=True, verbose_name="Customer Address")
    ADVOCATE_NAME          = models.CharField(max_length=200, blank=True, null=True, verbose_name="Advocate Name")
    ARBITRATOR_NAME        = models.CharField(max_length=200, blank=True, null=True, verbose_name="Arbitrator Name")
    ARBITRATOR_ADDRESS     = models.TextField(blank=True, null=True, verbose_name="Arbitrator Address")
    LRN_DATE               = models.DateField(blank=True, null=True, verbose_name="LRN Date")
    LRN_REFERENCE_NO       = models.CharField(max_length=100, blank=True, null=True, verbose_name="LRN Reference Number")
    LOAN_AMOUNT            = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Loan Amount (₹)")
    LOAN_AGREEMENT_DATE    = models.DateField(blank=True, null=True, verbose_name="Loan Agreement Date")
    PENDING_DUE_AMOUNT         = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Pending Due Amount (₹)")
    TOTAL_OUTSTANDING_AMOUNT   = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Total Outstanding Amount (₹)")
    OUTSTANDING_AMOUNT_ON_DATE = models.DateField(blank=True, null=True, verbose_name="Outstanding Amount on Date")
    PRODUCT_NAME               = models.CharField(max_length=200, blank=True, null=True, verbose_name="Product Name")

    class Meta:
        verbose_name = "Bulk Upload Case"
        verbose_name_plural = "Bulk Upload Cases"

class Bulk_Upload_Cases_PartyDetails(SoftDeleteTimestampMixin, models.Model):
    BULK_UPLOAD_CASE           = models.ForeignKey("bank_user.Bulk_Upload_Cases", on_delete=models.CASCADE,null=True,blank=True)
    PARTY_NAME                 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Party Name")
    PARTY_ADDRESS              = models.TextField(blank=True, null=True, verbose_name="Party Address")
      
    class Meta:
        verbose_name = "Bulk Upload Case Party Details"
        verbose_name_plural = "Bulk Upload Case Party Details"
