from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Unit(models.Model):

    class Meta:
        verbose_name_plural = "หน่วยขึ้นตรง ทอ. [Unit]" 
    FullName = models.CharField(max_length = 100, blank = False, default = None)
    ShortName = models.CharField(max_length = 100, blank = False, default = None)
    
    def __str__(self):
        return f'{self.ShortName}'


class User(AbstractUser):
    class Meta:        
        permissions = (
            ("User_AF_CMO", "User AF CMO"),
            ("User_Unit_CMO", "User Unit CMO"),
            ("User_PMD", "User PMD"),        
            ("User_CRC", "User CRC"),        
            # ศูนย์ปฏิบัติการพลเรือน-ทหารศูนย์บรรเทาสาธารณภัย
            # Civilian-Military Operations Center Disaster Relief Center
            # Preventive Medicine Division
            # ศูนย์ประสานผู้ป่วย COVID -19  ทอ. (RTAF COVID-19 Response Center : CRC)
        )
    CHOICE_Rank = (
        ( 30101 ,  'พล.อ.อ.*' ) ,
        ( 30102 ,  'พล.อ.อ.*หญิง' ) ,
        ( 30211 ,  'พล.อ.อ.' ) ,
        ( 30212 ,  'พล.อ.อ.หญิง' ) ,
        ( 30221 ,  'พล.อ.ท.' ) ,
        ( 30222 ,  'พล.อ.ท.หญิง' ) ,
        ( 30231 ,  'พล.อ.ต.' ) ,
        ( 30232 ,  'พล.อ.ต.หญิง' ) ,
        ( 30301 ,  'น.อ.(พ)' ) ,
        ( 30302 ,  'น.อ.(พ) หญิง' ) ,
        ( 30411 ,  'น.อ.' ) ,
        ( 30412 ,  'น.อ.หญิง' ) ,
        ( 30421 ,  'น.ท.' ) ,
        ( 30422 ,  'น.ท.หญิง' ) ,
        ( 30431 ,  'น.ต.' ) ,
        ( 30432 ,  'น.ต.หญิง' ) ,
        ( 30511 ,  'ร.อ.' ) ,
        ( 30512 ,  'ร.อ.หญิง' ) ,
        ( 30521 ,  'ร.ท.' ) ,
        ( 30522 ,  'ร.ท.หญิง' ) ,
        ( 30531 ,  'ร.ต.' ) ,
        ( 30532 ,  'ร.ต.หญิง' ) ,
        ( 30541 ,  'กห.ส.' ) ,
        ( 30542 ,  'กห.ส.หญิง' ) ,
        ( 30611 ,  'พ.อ.อ.(พ)' ) ,
        ( 30612 ,  'พ.อ.อ.(พ) หญิง' ) ,
        ( 30711 ,  'พ.อ.อ.' ) ,
        ( 30712 ,  'พ.อ.อ.หญิง' ) ,
        ( 30721 ,  'พ.อ.ท.' ) ,
        ( 30722 ,  'พ.อ.ท.หญิง' ) ,
        ( 30731 ,  'พ.อ.ต.' ) ,
        ( 30732 ,  'พ.อ.ต.หญิง' ) ,
        ( 30811 ,  'จ.อ.' ) ,
        ( 30812 ,  'จ.อ.หญิง' ) ,
        ( 30821 ,  'จ.ท.' ) ,
        ( 30822 ,  'จ.ท.หญิง' ) ,
        ( 30831 ,  'จ.ท.' ) ,
        ( 30832 ,  'จ.ต.หญิง' ) ,
        ( 30841 ,  'กห.ป.' ) ,
        ( 30842 ,  'กห.ป.หญิง' ) ,
        ( 31411 ,  'ว่าที่ น.อ.' ) ,
        ( 31412 ,  'ว่าที่ น.อ.หญิง' ) ,
        ( 31421 ,  'ว่าที่ น.ท.' ) ,
        ( 31422 ,  'ว่าที่ น.ท.หญิง' ) ,
        ( 31431 ,  'ว่าที่ น.ต.' ) ,
        ( 31432 ,  'ว่าที่ น.ต.หญิง' ) ,
        ( 31511 ,  'ว่าที่ ร.อ.' ) ,
        ( 31512 ,  'ว่าที่ ร.อ.หญิง' ) ,
        ( 31521 ,  'ว่าที่ ร.ท.' ) ,
        ( 31522 ,  'ว่าที่ ร.ท.หญิง' ) ,
        ( 31531 ,  'ว่าที่ ร.ต.' ) ,
        ( 31532 ,  'ว่าที่ ร.ต.หญิง' ) ,
        ( 40200 ,  'พนง.อาวุโสหญิง' ) ,
        ( 40201 ,  'พนง.อาวุโส' ) ,
        ( 40400 ,  'พนง.หญิง' ) ,
        ( 40401 ,  'พนง.' ) ,
        ( 50000 ,  '----' )
    ) 

    Rank = models.PositiveIntegerField(choices = CHOICE_Rank, default = 0, null=True)
    Position  =  models.CharField(max_length=250, null = True, blank = True)
    OfficePhone =  models.CharField(max_length=10, null = True, blank = True)
    MobileTel =  models.CharField(max_length=20, null = True, blank = True)
    Unit =  models.CharField(max_length=150, null = True, blank = True)    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



