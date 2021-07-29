from django.contrib import admin

from Patient.models import ( Patient, 
                             TreatmentLog, 
                             StatusLog,
                             AMEDPatient)

class PatientAdmin(admin.ModelAdmin):
    list_display = ['Date','FullName','PersonID','AirforceType','Office']
    search_fields = ['FullName']
    list_filter = ['Date','CurrentStatus','CurrentTreatment']
    list_editable = ['AirforceType','Office']
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
    list_display = ['FullName','PersonID','HNNumber','ANNumber','Mobile','RightMedicalTreatment']
    list_display_links = ['FullName']
    search_fields = ['FullName','PersonID']
    list_editable = ['HNNumber','ANNumber']
    # list_filter = ['Date']
    # save_as = True
    # list_editable = ['Type','NumDay']
    # list_display_links = ['Person']    

admin.site.register(Patient, PatientAdmin)
admin.site.register(TreatmentLog, TreatmentLogAdmin)
admin.site.register(StatusLog, StatusLogAdmin)
admin.site.register(AMEDPatient, AMEDPatientAdmin)
