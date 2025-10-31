from django.db import models

# Create your models here.

from django.db import models


class SoftDeleteTimestampMixin(models.Model):
    IS_DELETED      = models.BooleanField(default=False, db_index=True)
    CREATED_DATE    = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    UPDATED_DATE    = models.DateTimeField(auto_now=True, null=True, blank=True)

    def delete(self, *args, **kwargs):
        """Soft delete the record instead of removing it."""
        self.IS_DELETED = True
        self.save(update_fields=["IS_DELETED", "UPDATED_DATE"])

    class Meta:
        abstract = True


class StateMaster(SoftDeleteTimestampMixin):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    CODE = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "State Master"

    def __str__(self):
        return self.NAME or "Unnamed State"


class CityMaster(SoftDeleteTimestampMixin,models.Model):
    STATE          = models.ForeignKey("master.StateMaster", on_delete=models.CASCADE,null=True,blank=True)
    NAME            = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        verbose_name_plural = "City Master"