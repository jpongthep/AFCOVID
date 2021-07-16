from django.db import models
from django.db.models.fields import BooleanField
from UserData.models import User
import datetime

# Create your models here.



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
    EmergencyMobileMobile  = models.CharField(
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
                                    null = True,)
    Comment  = models.TextField(
                                default = None, 
                                verbose_name = "คำอธิบาย",
                                blank = True, 
                                null = True,)

    def __str__(self):
        return self.FullName

    @property
    def CurrentStatus(self):
        LastestStatus = StatusLog.objects.filter(Patient = self).order_by('-Date')
        if LastestStatus.exists():
            return LastestStatus[0].get_Status_display()
        else:
            return "-"

    
    @property
    def CurrentTreatment(self):
        LastestTreatment = TreatmentLog.objects.filter(Patient = self).order_by('-Date')
        if LastestTreatment.exists():
            return LastestTreatment[0].get_Treatment_display()
        else:
            return "-"
    

class StatusLog(models.Model):
    class Meta:
        verbose_name_plural = "ตารางสถานะผู้ป่วย [StatusLog]"    
        # ordering = ('-ActionOccure','ActionUser','ActionDo')
        #     
    Patient  = models.ForeignKey(
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
    CHOICE_STATUSLEVEL = (
        ( 1 ,  'เขียว' ) ,
        ( 2 ,  'เหลืองอ่อน' ) ,
        ( 3 ,  'เหลืองแก่' ) ,
        ( 4 ,  'แดง' ) ,
        ( 5 ,  'หายป่วย' ) ,
        ( 6 ,  'เสียชีวิต' ) ,
        ( 7 ,  'เสี่ยงสูง (ผู้ใกล้ชิด)' ) ,
        ( 8 ,  'ปลอดเชื้อ (ผู้ใกล้ชิด)' ) ,
        ( 9 ,  'ติดเชื้อ (ผู้ใกล้ชิด)' ) ,
    ) 
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
        return f'{self.Patient} : {self.Status}'

class TreatmentLog (models.Model):
    class Meta:
        verbose_name_plural = "ตารางแสดงการรักษาผู้ป่วย [TreatmentLog]"

    Patient  = models.ForeignKey(
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
    TREATMENTCHOICES = (
        ( 1 ,  'รักษาระยะห่าง'),
        ( 2 ,  'กักตัวอยู่บ้าน'),
        ( 3 ,  'กักตัวรอเตียง'),
        ( 4 ,  'Home Isolation'),
        ( 5 ,  'รพ.สนาม'),
        ( 6 ,  'โรงพยาบาล'),
        ( 7 ,  'ICU')
    ) 
    Treatment = models.IntegerField(
                                choices = TREATMENTCHOICES, 
                                default = 1, 
                                null=True)
    Comment  = models.TextField(default = None, 
                                verbose_name = "คำอธิบาย",
                                null=True,
                                blank = True)

    def __str__(self):
        return f'{self.Patient} : {self.Treatment}'