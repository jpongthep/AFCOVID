from django.contrib import admin
from .models import  DateTimeSlot, Queue

class DateTimeSlotAdmin(admin.ModelAdmin):
    list_display = ['date_reserve','get_slot_display','number_queue','reserve_queue']
    # list_display_links = ['FullName',]
    # date_hierarchy = 'DateReport'
    # search_fields = ['FullName']
    # list_filter = ['DateReport']
    # # # list_editable = ['Type','NumDay']

class QueueAdmin(admin.ModelAdmin):
    list_display = ['date_reserve','get_slot_display','queue_number','person_id']
    # list_display_links = ['FullName',]
    # date_hierarchy = 'DateReport'
    # search_fields = ['FullName']
    # list_filter = ['DateReport']
    # # # list_editable = ['Type','NumDay']
    
    
admin.site.register(Queue, QueueAdmin)
admin.site.register(DateTimeSlot, DateTimeSlotAdmin)