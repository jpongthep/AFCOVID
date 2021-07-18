from datetime import date
import datetime

from django.db import models
from django.db.models.fields import BooleanField
from django.db.models.signals import post_save

from UserData.models import User
# Create your models here.

CHOICE_STATUSLEVEL = (
    ( 0 ,  'ไม่ระบุ' ) ,
    ( 1 ,  'ผู้ป่วยสีเขียว' ) ,
    ( 2 ,  'ผู้ป่วยสีเหลือง' ) ,
    ( 3 ,  'ผู้ป่วยสีส้ม' ) ,
    ( 4 ,  'ผู้ป่วยสีแดง' ) ,
    ( 5 ,  'หายป่วย' ) ,
    ( 6 ,  'เสียชีวิต' ) ,
    ( 7 ,  'ผู้ใกล้ชิดเสี่ยงสูง' ) ,
    ( 8 ,  'ผู้ใกล้ชิดปลอดเชื้อ' ) ,
    ( 9 ,  'ผู้ใกล้ชิดติดเชื้อ' ) ,
)

TREATMENTCHOICES = (
    ( 0 ,  'ไม่ระบุ'),
    ( 1 ,  'รักษาระยะห่าง'),
    ( 2 ,  'กักตัวอยู่บ้าน'),
    ( 3 ,  'กักตัวรอเตียง'),
    ( 4 ,  'Home Isolation'),
    ( 5 ,  'รพ.สนาม'),
    ( 6 ,  'โรงพยาบาล'),
    ( 7 ,  'ICU')
) 

class Patient(models.Model):
    class Meta:
        verbose_name_plural = "ตารางผู้ป่วย [Patient]"    
        # ordering = ('-ActionOccure','ActionUser','ActionDo')
        
    Date = models.DateField(
                            default=datetime.date.today, 
                            verbose_name = 'วันที่')
    DataUser = models.ForeignKey(
                                User, 
                                on_delete=models.DO_NOTHING, 
                                related_name='DataUser', 
                                verbose_name = 'ผู้บันทึก')
    FullName = models.CharField(                                
                                max_length = 255,
                                default = "-", 
                                blank = True, 
                                null = True,
                                verbose_name = 'ชื่อผู้ป่วย')
    InfectiousName = models.ForeignKey(
                                    'self', 
                                    on_delete=models.DO_NOTHING, 
                                    related_name='Infectious_Name', 
                                    blank = True, 
                                    null = True,
                                    verbose_name = 'ชื่อคนแพร่เชื้อ')
    CHOICE_Gender = (
        ( '-' ,  'ไม่ระบุ' ) ,
        ( 'ช' ,  'ชาย' ) ,
        ( 'ญ' ,  'หญิง' ) ,
    ) 
    Gender = models.CharField(
                            max_length = 8,
                            choices = CHOICE_Gender, 
                            default = '-', 
                            null=True,
                            blank = True)
    BirthDay  = models.DateField(
                                blank = True, 
                                null = True,
                                verbose_name = 'วันเกิด')
    PersonID = models.CharField(
                                max_length = 13,
                                default = "-", 
                                blank = True, 
                                null = True,
                                verbose_name = 'เลขบัตรประชาชน')
    Office = models.TextField(
                            default = None, 
                            verbose_name = 'ที่ทำงาน/สังกัด',
                            blank = True, 
                            null = True,)
    IsAirforce = BooleanField(
                                    default = False, 
                                    verbose_name= "ขรก.ทอ.",
                                    blank = True, 
                                    null = True,)
    DatePositive  = models.DateField(
                                    blank = True, 
                                    null = True,
                                    verbose_name = 'วันที่ตรวจพบเชื้อ')
    CurrentStatus = models.IntegerField(
                            choices = CHOICE_STATUSLEVEL, 
                            default = 0, 
                            null=True,
                            blank = True)
    CurrentTreatment = models.IntegerField(
                                choices = TREATMENTCHOICES, 
                                default = 0, 
                                null=True)                                                          
    Mobile  = models.CharField(
                                max_length = 20,
                                blank = True, 
                                null = True,
                                verbose_name = 'เบอร์มือถือ')
    Address = models.TextField(
                                default = None, 
                                verbose_name = 'ที่อยู่ปัจจุบัน', 
                                null = True, 
                                blank = True)
    Corona3 = models.FileField(
                                upload_to='Corona3/', 
                                null = True, 
                                blank = True)
    DetectedResult  = models.FileField(
                                    upload_to='Corona3/', 
                                    null = True, 
                                    blank = True)
    EmergencyMobile  = models.CharField(
                                            max_length = 20,
                                            blank = True, 
                                            null = True,
                                            verbose_name = 'เบอร์ฉุกเฉิน')
    ConfirmUser = models.ForeignKey(
                                User, 
                                on_delete=models.DO_NOTHING, 
                                related_name='ConfirmUser', 
                                verbose_name = 'ผู้ยืนยันข้อมูล ',
                                null = True,
                                blank = True)
    ConfirmedPatient = BooleanField(
                                    default = False, 
                                    verbose_name= "กวป.ยืนยันผู้ติดเชื้อ",
                                    blank = True, 
                                    null = True)
    Comment  = models.TextField(
                                default = None, 
                                verbose_name = "คำอธิบาย",
                                blank = True, 
                                null = True,)


    def __str__(self):
        return self.FullName

    # @property
    # def CurrentStatus(self):
    #     LastestStatus = StatusLog.objects.filter(Patient = self).order_by('-Date')
    #     if LastestStatus.exists():
    #         return LastestStatus[0].get_Status_display()
    #     else:
    #         return "-"
    
    @property
    def LestestStatus(self):
        LastestStatus = StatusLog.objects.filter(ThePatient = self).order_by('-Date')
        if LastestStatus.exists():
            return LastestStatus[0].Date
        else:
            return ""

    
    # @property
    # def CurrentTreatment(self):
    #     LastestTreatment = TreatmentLog.objects.filter(Patient = self).order_by('-Date')
    #     if LastestTreatment.exists():
    #         return LastestTreatment[0].get_Treatment_display()
    #     else:
    #         return "-"
    
    @property
    def LestestTreatment(self):
        LastestTreatment = TreatmentLog.objects.filter(ThePatient = self).order_by('-Date')
        if LastestTreatment.exists():
            return LastestTreatment[0].Date
        else:
            return ""

    @property
    def Age(self):
        if self.BirthDay:
            today = date.today()
            return today.year - self.BirthDay.year
        else:
            return "-"
    

class StatusLog(models.Model):
    class Meta:
        verbose_name_plural = "ตารางสถานะผู้ป่วย [StatusLog]"    
        # ordering = ('-ActionOccure','ActionUser','ActionDo')
        #     
    ThePatient  = models.ForeignKey(
                                Patient, 
                                on_delete=models.DO_NOTHING, 
                                related_name='PatientName', 
                                blank = True, 
                                null = True,
                                verbose_name = 'ชื่อผู้ป่วย')
    RecorderUser =  models.ForeignKey(
                                User, 
                                on_delete=models.DO_NOTHING, 
                                related_name='StatusRecorderUser', 
                                verbose_name = 'ผู้บันทึกข้อมูล')
    Date = models.DateField(blank = True, 
                            null = True,
                            verbose_name = 'วันที่บันทึก')

    Status = models.IntegerField(
                            choices = CHOICE_STATUSLEVEL, 
                            default = 1, 
                            null=True,
                            blank = True)
    Comment  = models.TextField(default = None, 
                                verbose_name = "คำอธิบาย",
                                null=True,
                                blank = True)

    def __str__(self):
        return f'{self.ThePatient} : {self.Status}'

class TreatmentLog(models.Model):
    class Meta:
        verbose_name_plural = "ตารางแสดงการรักษาผู้ป่วย [TreatmentLog]"

    ThePatient  = models.ForeignKey(
                                    Patient, 
                                    on_delete=models.DO_NOTHING, 
                                    related_name='PatientLogTreament', 
                                    blank = True, 
                                    null = True,
                                    verbose_name = 'ชื่อผู้ป่วย')
    RecorderUser =  models.ForeignKey(
                                    User, 
                                    on_delete=models.DO_NOTHING, 
                                    related_name='TreatmentLogUser', 
                                    verbose_name = 'ผู้บันทึกข้อมูล')
    Date = models.DateField(blank = True, 
                            null = True,
                            verbose_name = 'วันที่บันทึก')

    Treatment = models.IntegerField(
                                choices = TREATMENTCHOICES, 
                                default = 1, 
                                null=True)
    Comment  = models.TextField(default = None, 
                                verbose_name = "คำอธิบาย",
                                null=True,
                                blank = True)

    def __str__(self):
        return f'{self.ThePatient} : {self.Treatment}'

