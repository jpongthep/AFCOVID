from django.contrib import admin

from Corona3.models import ( Corona3)
# , TreatmentLog, StatusLog)

class Corona3Admin(admin.ModelAdmin):
    list_display = ['Date','FullName']
    # ,'CurrentStatus','CurrentTreatment']
    search_fields = ['FullName']
    list_filter = ['DatePatient']
    # list_editable = ['Type','NumDay']
    # list_display_links = ['Person']


# class StatusLogAdmin(admin.ModelAdmin):
#     list_display = ['ThePatient','Date','Status']
#     search_fields = ['ThePatient__FullName']
#     list_filter = ['Date']
#     save_as = True
    # list_editable = ['Type','NumDay']
    # list_display_links = ['Person']

# class TreatmentLogAdmin(admin.ModelAdmin):
#     list_display = ['ThePatient','Date','Treatment']
#     search_fields = ['ThePatient__FullName']
#     list_filter = ['Date']
#     save_as = True
    # list_editable = ['Type','NumDay']
    # list_display_links = ['Person']

admin.site.register(Corona3, Corona3Admin)
# admin.site.register(TreatmentLog, TreatmentLogAdmin)
# admin.site.register(StatusLog, StatusLogAdmin)
