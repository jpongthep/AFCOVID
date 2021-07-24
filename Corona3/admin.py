from django.contrib import admin

from Corona3.models import ( Corona3)
# , TreatmentLog, StatusLog)

@admin.action(description='Mark selected Corona3 ')
def MakeGender(modeladmin, request, queryset):
    queryset.update(Gender='ช')
    

class Corona3Admin(admin.ModelAdmin, ):
    list_display = ['DatePatient','FullName', 'Gender']
    # ,'CurrentStatus','CurrentTreatment']
    search_fields = ['FullName']
    list_filter = ['DatePatient']
    actions = [MakeGender]

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
