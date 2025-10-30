from django.contrib import admin
from master.models import StateMaster, CityMaster

# Register your models here.

@admin.register(StateMaster)
class StateMasterAdmin(admin.ModelAdmin):
    list_display = ["id","NAME"]
    search_fields = ['id','NAME']


@admin.register(CityMaster)
class CityMasterAdmin(admin.ModelAdmin):
    list_display = ["id",'get_state_name',"NAME"]
    search_fields = ['id','NAME']

    def get_state_name(self, obj):
        return obj.STATE.NAME
    get_state_name.short_description = 'State Name'