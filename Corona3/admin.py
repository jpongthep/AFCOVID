from django.contrib import admin

from Corona3.models import  Corona3
from Patient.models import  Patient

class Corona3Admin(admin.ModelAdmin):
    list_display = ['DateReport','FullName','PersonID','Age']
    list_display_links = ['FullName',]
    date_hierarchy = 'DateReport'
    search_fields = ['FullName']
    list_filter = ['DateReport']
    # # list_editable = ['Type','NumDay']
    

admin.site.register(Corona3, Corona3Admin)
