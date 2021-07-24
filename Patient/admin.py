from django.contrib import admin
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME

from django.contrib import messages
from django.utils.translation import ngettext

from Patient.models import ( Patient, 
                             TreatmentLog, 
                             StatusLog,
                             AMEDPatient)

# @admin.action(description='เปลี่ยนเป็นหายป่วย ')
# def MakeGood(modeladmin, request, queryset):
#     queryset.update(CurrentStatus='5')


@admin.action(description='เปลี่ยนจากการรักษาเป็นรักษาระยะห่าง ')
def Make(modeladmin, request, queryset):
    queryset.update(CurrentTreatment='1')

class PatientAdmin(admin.ModelAdmin):
    list_display = ['Date','FullName','PersonID','CurrentStatus','CurrentTreatment']
    search_fields = ['FullName']
    list_filter = ['Date']
    # actions = [MakeGood]
    actions = [Make]

    # @admin.action(description='เปลี่ยนเป็นหายป่วย ')
    # def MakeGood(self, request, queryset):
    #     updated = queryset.update(CurrentStatus='5')
    #     self.message_user(request, ngettext(
    #         '%d story was successfully marked as CurrentStatus.',
    #         '%d stories were successfully marked as CurrentStatus.',
    #         updated,
    #     ) % updated, messages.SUCCESS)
    # actions = [MakeGood]


    # @admin.action(description='เปลี่ยนจากการรักษาเป็นรักษาระยะห่าง ')
    # def Make(self, request, queryset):
    #     updated = queryset.update(CurrentTreatment='1')
    #     self.message_user(request, ngettext(
    #         '%d story was successfully marked as CurrentTreatment.',
    #         '%d stories were successfully marked as CurrentTreatment.',
    #         updated,
    #     ) % updated, messages.SUCCESS)
    # actions = [Make]

    
    list_filter = ['Date','CurrentStatus','CurrentTreatment']
    # list_editable = ['Type','NumDay']
    list_display_links = ['FullName',]


class StatusLogAdmin(admin.ModelAdmin):
    list_display = ['ThePatient','Date','Status']
    search_fields = ['ThePatient__FullName']
    list_filter = ['Date']
    save_as = True
    # list_editable = ['Type','NumDay']
    # list_display_links = ['Person']

class TreatmentLogAdmin(admin.ModelAdmin):
    list_display = ['ThePatient','Date','Treatment']
    search_fields = ['ThePatient__FullName']
    list_filter = ['Date']
    save_as = True
    # list_editable = ['Type','NumDay']
    # list_display_links = ['Person']

class AMEDPatientAdmin(admin.ModelAdmin):
    list_display = ['FullName','PersonID','HNNumber','ANNumber','Mobile']
    list_display_links = ['FullName']
    search_fields = ['FullName']
    list_editable = ['HNNumber','ANNumber']
    # list_filter = ['Date']
    # save_as = True
    # list_editable = ['Type','NumDay']
    # list_display_links = ['Person']    

admin.site.register(Patient, PatientAdmin)
admin.site.register(TreatmentLog, TreatmentLogAdmin)
admin.site.register(StatusLog, StatusLogAdmin)
admin.site.register(AMEDPatient, AMEDPatientAdmin)
