from django.contrib import admin

from Patient.models import ( Patient, 
                             TreatmentLog, 
                             StatusLog)

class PatientAdmin(admin.ModelAdmin):
    list_display = ['Date','FullName','PersonID','CurrentStatus','CurrentTreatment']
    search_fields = ['FullName']
    list_filter = ['Date']
    # list_editable = ['Type','NumDay']
    # list_display_links = ['Person']


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

admin.site.register(Patient, PatientAdmin)
admin.site.register(TreatmentLog, TreatmentLogAdmin)
admin.site.register(StatusLog, StatusLogAdmin)
