import datetime

from django.utils import timezone
from django.db.models.constraints import UniqueConstraint
from django.db import models

from UserData.models import User

def tomorrow():
    _tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return _tomorrow

class Slot(models.TextChoices):
        NOTSELECT = '--', "-------"
        SL08 = '08', "0800 - 0900"
        SL09 = '09', "0900 - 1000"
        SL10 = '10', "1000 - 1100"
        SL11 = '11', "1100 - 1200"
        SL13 = '13', "1300 - 1400"
        
class DateTimeSlot(models.Model):
    class Meta:
        verbose_name_plural = "ตารางวันเวลา [DateTimeSlot]"
        constraints = [
            UniqueConstraint(fields=['date_reserve', 'slot'], name='date_slot')
        ]
        ordering = ('-date_reserve','slot')
    
    date_reserve = models.DateField(verbose_name = 'วันจอง', default=tomorrow, )
    slot = models.CharField(verbose_name = 'ช่วงเวลา',max_length = 2,choices = Slot.choices, 
                            default = Slot.NOTSELECT,null=True,blank = True)
    number_queue = models.IntegerField(verbose_name = 'จำนวนคิว', default = 200, null=True, blank = True)   
    reserve_queue = models.IntegerField(verbose_name = 'จองแล้ว', default = 0, null=True, blank = True)   
    update_user = models.ForeignKey(User, verbose_name = 'ผู้แก้ไขข้อมูล ', on_delete=models.SET_NULL, 
                                    related_name='updater', null = True,blank = True)
    def __str__(self):
        return str(self.date_reserve) + ' : ' + self.get_slot_display()

class Queue(models.Model):
    class Meta:
        verbose_name_plural = "ตารางจองคิว [Queue]"
        constraints = [
            UniqueConstraint(fields = ['date_reserve', 'slot','queue_number'], 
                            name = 'date_slot_queue')
        ]
        ordering = ('-date_reserve','slot','-queue_number')
    
    date_reserve = models.DateField(verbose_name = 'วันจอง', default=tomorrow, )
    slot = models.CharField(verbose_name = 'ช่วงเวลา',max_length = 2,choices = Slot.choices, 
                            default = Slot.NOTSELECT)
    queue_number = models.IntegerField(verbose_name = 'เลขที่คิว', default = 0)   
    person_id = models.CharField(verbose_name = 'เลขบัตรประชาชน', max_length = 13)
    is_present = models.BooleanField(verbose_name= "เข้าตรวจ",default = True, blank = True, null = True,)
    created     = models.DateTimeField(editable=False, blank = True)
    modified    = models.DateTimeField(blank = True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Queue, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.date_reserve:%d-%m} SL-{self.slot}: Q {self.queue_number:03d}'
  