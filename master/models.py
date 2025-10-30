from django.db import models

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


class StateMaster(SoftDeleteTimestampMixin,models.Model):
    NAME            = models.CharField(max_length=100,null=True,blank=True)
    CODE            = models.CharField(max_length=100,null=True,blank=True)
    
    class Meta:
        verbose_name_plural = "State Master"

class CityMaster(SoftDeleteTimestampMixin,models.Model):
    STATE          = models.ForeignKey("master.StateMaster", on_delete=models.CASCADE,null=True,blank=True)
    NAME            = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        verbose_name_plural = "City Master"