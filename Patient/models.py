from datetime import date
import datetime

from django.db import models
from django.db.models.fields import BooleanField

from UserData.models import User

AIRFORCE_TYPE_CHOICE = (
    ( 0 ,  'ไม่ระบุ' ) ,
    ( 1 ,  'ทหารประจำการ' ) ,
    ( 2 ,  'พลทหาร' ) ,
    ( 3 ,  'พนง.ราชการ' ) ,
    ( 4 ,  'ลูกจ้างประจำ' ) ,
    ( 5 ,  'ลูกจ้างชั่วคราว' ) ,
    ( 6 ,  'ครอบครัว ทอ.' ) ,
    ( 7 ,  'บุคคลภายนอก' ) ,
)

RIGHT_MEDICAL_TREATMENT_CHOICE = (
    ( 0 ,  'ไม่ระบุ' ) ,
    ( 1 ,  'เบิกจ่ายตรง (กรมบัญชีกลาง)' ) ,
    ( 2 ,  'ประกันสังคม' ) ,
    ( 3 ,  'UC (สปสช.)' ) ,
    ( 4 ,  'เงินสด' ) ,
)

CHOICE_STATUSLEVEL = (
    ( 0 ,  'ไม่ระบุ' ) ,
    ( 1 ,  'ผู้ป่วยสีเขียว' ) ,
    ( 2 ,  'ผู้ป่วยสีเหลืองอ่อน' ) ,
    ( 3 ,  'ผู้ป่วยสีเหลืองเข้ม' ) ,
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
                                unique = True,
                                blank = True, 
                                null = True,
                                verbose_name = 'เลขบัตรประชาชน')
    Office = models.CharField(
                            max_length = 50,
                            default = None, 
                            verbose_name = 'ที่ทำงาน/สังกัด',
                            blank = True, 
                            null = True,)
    AirforceType = models.IntegerField(
                            choices = AIRFORCE_TYPE_CHOICE, 
                            default = 0, 
                            null=True,
                            verbose_name = 'ประเภทข้าราชการ')                             
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
                            verbose_name = 'สถานะผู้ป่วยปัจจุบัน')
    CurrentTreatment = models.IntegerField(
                                choices = TREATMENTCHOICES, 
                                default = 0, 
                                null=True,
                                verbose_name = 'การรักษาปัจจุบัน')                                                         
    Mobile  = models.CharField(
                                max_length = 10,
                                blank = True, 
                                null = True,
                                verbose_name = 'เบอร์มือถือ')
    Address = models.TextField(
                                default = None, 
                                verbose_name = 'ที่อยู่ปัจจุบัน', 
                                null = True, 
                                blank = True)
    RightMedicalTreatment = models.IntegerField(
                            choices = RIGHT_MEDICAL_TREATMENT_CHOICE, 
                            default = 0, 
                            verbose_name = 'สิทธิ์การรักษาพยาบาล', 
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
                                            max_length = 10,
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
    ConfirmedByCRC = BooleanField(
                                    default = False, 
                                    verbose_name= "แพทย์ยืนยันข้อมูล",
                                    blank = True, 
                                    null = True)
    IsAMED = BooleanField(
                                    default = False, 
                                    verbose_name= "มีข้อมูลใน AMED",
                                    blank = True, 
                                    null = True,)                                    
    Comment  = models.TextField(
                                default = None, 
                                verbose_name = "หมายเหตุ",
                                blank = True, 
                                null = True,)


    def __str__(self):
        return self.FullName

    @property
    def IsPersonID(self):
        if self.PersonID:
            return len(self.PersonID) == 13
        else:
            return False
    @property
    def IsMobile(self):
        if self.Mobile:
            return len(self.Mobile) == 10
        else:
            return False

    @property
    def Age(self):
        if self.BirthDay:
            today = date.today()
            return today.year - self.BirthDay.year
        else:
            return "-"

    
    @property
    def TreatmentIcon(self):
        if self.CurrentTreatment == 0:
            return f'<abbr title="{self.get_CurrentTreatment_display()}"><i class="fa fa-question-circle fa-lg" style="color:rgb(160,160,160)"></i></abbr>'
        elif self.CurrentTreatment == 1:
            return f'<abbr title="{self.get_CurrentTreatment_display()}"><i class="fa fa-male fa-lg" style="color:rgb(246,199,0)"></i>---<i class="fa fa-male fa-lg" style="color:green"></i></abbr>'
        elif self.CurrentTreatment == 2:
            return f'<abbr title="{self.get_CurrentTreatment_display()}"><i class="fa fa-home fa-lg" style="color:green"></i></abbr>'
        elif self.CurrentTreatment == 3:
            return f'<abbr title="{self.get_CurrentTreatment_display()}"><i class="fa fa-home fa-lg" style="color:yellow"></i></abbr>'
        elif self.CurrentTreatment == 4:
            return f'<abbr title="{self.get_CurrentTreatment_display()}"><i class="fa fa-home fa-lg" style="color:black"></i></abbr>'
        elif self.CurrentTreatment == 5:
            return f'<abbr title="{self.get_CurrentTreatment_display()}"><i class="fa fa-hospital-symbol fa-lg" style="color:green"></i></abbr>'
        elif self.CurrentTreatment == 6:
            return f'<abbr title="{self.get_CurrentTreatment_display()}"><i class="fa fa-hospital fa-lg" style="color:yellow"></i></abbr>'
        elif self.CurrentTreatment == 7:
            return f'<abbr title="{self.get_CurrentTreatment_display()}"><i class="fa fa-hospital fa-lg" style="color:red"></i></abbr>'
    
class StatusLog(models.Model):
    class Meta:
        verbose_name_plural = "ตารางสถานะผู้ป่วย [StatusLog]"    
        # ordering = ('-ActionOccure','ActionUser','ActionDo')
        #     
    ThePatient  = models.ForeignKey(
                                Patient, 
                                on_delete=models.CASCADE, 
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
                                    on_delete=models.CASCADE, 
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


class AMEDPatient(models.Model):
    class Meta:
        verbose_name_plural = "ตารางผู้ป่วย AMED [AMED Patient]"
    PersonID = models.CharField(
                                max_length = 13,
                                unique = True,
                                blank = True, 
                                null = True,
                                verbose_name = 'เลขบัตรประชาชน')
    HNNumber = models.CharField(
                                max_length = 20,
                                blank = True,
                                null = True,
                                verbose_name = 'เลขผู้ป่วยนอก')
    ANNumber = models.CharField(
                                max_length = 20,
                                blank = True,
                                null = True,
                                verbose_name = 'เลขผู้ป่วยใน')
    FullName = models.CharField(                                
                                max_length = 255,
                                default = "-", 
                                blank = True, 
                                null = True,
                                verbose_name = 'ชื่อผู้ป่วย')
    Mobile = models.CharField(
                                max_length = 10,
                                blank = True, 
                                null = True,
                                verbose_name = 'เบอร์มือถือ')
    RightMedicalTreatment = models.IntegerField(
                            choices = RIGHT_MEDICAL_TREATMENT_CHOICE, 
                            default = 0, 
                            verbose_name = 'สิทธิ์การรักษาพยาบาล', 
                            null = True,
                            blank = True)                                
    Symtom = models.IntegerField(
                                choices = CHOICE_STATUSLEVEL, 
                                default = 0, 
                                null=True)

    Report  = models.TextField(verbose_name = "รายงานใน AMED",
                                null=True,
                                blank = True)                                
    Comment  = models.TextField(verbose_name = "คำอธิบาย",
                                null=True,
                                blank = True)                                

    def __str__(self):
        return self.FullName

    @property
    def AmedSymtomIcon(self):
        if self.Symtom == 0:
            return f'<abbr title="{self.get_Symtom_display()}"><i class="fa fa-question-circle fa-lg" style="color:rgb(160,160,160)"></i></abbr>'
        elif self.Symtom == 1:
            return f'<abbr title="{self.get_Symtom_display()}"><i class="fas fa-address-book" style="color:green"></i></abbr>'
        elif self.Symtom == 2:
            return f'<abbr title="{self.get_Symtom_display()}"><i class="fas fa-address-book" style="color:yellow"></i></abbr>'
        elif self.Symtom == 3:
            return f'<abbr title="{self.get_Symtom_display()}"><i class="fas fa-address-book" style="color:gold"></i></abbr>'
        elif self.Symtom == 4:
            return f'<abbr title="{self.get_Symtom_display()}"><i class="fas fa-address-book" style="color:red"></i></abbr>'
        elif self.Symtom == 5:
            return f'<abbr title="{self.get_Symtom_display()}"><i class="fa fa-child fa-lg" style="color:blue"></i></abbr>'
        elif self.Symtom == 6:
            return f'<abbr title="{self.get_Symtom_display()}"><i class="fas fa-user-alt-slash" style="color:black"></i></abbr>'
        elif self.Symtom == 7:
            return f'<abbr title="{self.get_Symtom_display()}"><i class="fas fa-address-book" style="color:blue"></i></abbr>---<i class="fa fa-male fa-lg" style="color:gold"></i></abbr>'
   
        elif self.Symtom == 8:
            return f'<abbr title="{self.get_Symtom_display()}"><i class="fas fa-address-book" style="color:blue"></i></abbr>---<i class="fa fa-male fa-lg" style="color:blue"></i></abbr>'
   
        elif self.Symtom == 9:
            return f'<abbr title="{self.get_Symtom_display()}"><i class="fas fa-address-book" style="color:blue"></i></abbr>---<i class="fa fa-male fa-lg" style="color:red"></i></abbr>'
   
    @property
    def RightMedicalTreatmentIcon(self):
        if self.RightMedicalTreatment == 0:
            return f'<abbr title="{self.get_RightMedicalTreatment_display()}"><i class="fa fa-question-circle fa-lg" style="color:rgb(160,160,160)"></i></abbr>'
        elif self.RightMedicalTreatment == 1:
            return f'<abbr title="{self.get_RightMedicalTreatment_display()}"><i class="far fa-money-bill-alt" style="color:green"></i></abbr>---><i class="fas fa-school" style="color:blue"></i></abbr>'
        
        elif self.RightMedicalTreatment == 2:
            return f'<abbr title="{self.get_RightMedicalTreatment_display()}"><i class="far fa-money-bill-alt" style="color:blue"></i></abbr>'
        elif self.RightMedicalTreatment == 3:
            return f'<abbr title="{self.get_RightMedicalTreatment_display()}"><i class="far fa-money-bill-alt" style="color:yellow"></i></abbr>---><i class="fas fa-school" style="color:gold"></i></abbr>'
   
        elif self.RightMedicalTreatment == 4:
            return f'<abbr title="{self.get_RightMedicalTreatment_display()}"><i class="far fa-money-bill-alt" style="color:red"></i></abbr>'
            


