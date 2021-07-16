from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class Patient(models.Model):
    Date = models.DateField(default=datetime.date.today , verbose_name="วันที่บันทึกข้อมูล")
    DataUser = models.CharField(User, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=250, verbose_name="คำนำหน้า - ชื่อ - นามสกุล")
    
    GENDERCHOICE = [
        ('0', 'ไม่ระบุ')
        ('1', 'ผู้ชาย'),
        ('2', 'ผู้หญิง'),
    ]
    Gender = models.CharField(max_length = 10, choices=GENDERCHOICE, default='-', verbose_name="เพศ" )
    BirthDay = models.DateField()
