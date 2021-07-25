# Generated by Django 3.2.5 on 2021-07-25 04:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corona3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonID', models.CharField(max_length=13, unique=True, verbose_name='เลขบัตรประชาชน/พาสปอร์ต')),
                ('FullName', models.CharField(max_length=255, verbose_name='ชื่อผู้ป่วย')),
                ('Gender', models.CharField(blank=True, choices=[('-', 'ไม่ระบุ'), ('ช', 'ชาย'), ('ญ', 'หญิง')], default='-', max_length=8, null=True, verbose_name='เพศ')),
                ('BirthYear', models.IntegerField(verbose_name='พ.ศ.เกิด')),
                ('Nationality', models.CharField(blank=True, choices=[('0', 'ไม่ระบุ'), ('1', 'ไทย'), ('2', 'ลาว'), ('3', 'กัมพูชา'), ('4', 'พม่า'), ('5', 'จีน'), ('6', 'อินเดีย'), ('7', 'มาเลเซีย'), ('8', 'สิงค์โปร')], default='-', max_length=20, null=True, verbose_name='สัญชาติ')),
                ('TypeCheck', models.CharField(blank=True, choices=[('1', 'PUI'), ('2', 'ผู้สัมผัสใกล้ชิด'), ('3', 'การค้นหาสำรวจเชิงรุก'), ('4', 'Sentinet Surevellence'), ('5', 'อื่น ๆ (โปรดระบุข้อความ)')], default='-', max_length=100, null=True, verbose_name='ประเภทตรวจพบ')),
                ('TypeCheck_Other', models.CharField(blank=True, default='-', max_length=200, null=True, verbose_name='ระบุการตรวจพบจากกรณีอื่น ๆ')),
                ('CareerPatient', models.CharField(blank=True, default='-', max_length=3, null=True, verbose_name='อาชีพ(ระบุลักษณะงาน เช่น บุคลากรทางการแพทย์)')),
                ('PlaceWork', models.CharField(blank=True, default='-', max_length=250, null=True, verbose_name='สถานที่ทำงาน/สถานศึกษา')),
                ('Mobile', models.CharField(max_length=20, verbose_name='เบอร์มือถือ')),
                ('Address', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='ที่อยู่ปัจจุบัน')),
                ('Swine', models.IntegerField(blank=True, default='-', null=True, verbose_name='หมู่ที่')),
                ('SubDistrict', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='ตำบล/แขวง')),
                ('District', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='อำเภอ/เขต')),
                ('Province', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='จังหวัด')),
                ('ZipCode', models.CharField(blank=True, default='-', max_length=5, null=True, verbose_name='รหัสไปรษณีย์')),
                ('TypeLive', models.CharField(blank=True, choices=[('1', 'บ้านเดี่ยว'), ('2', 'ตึกแถว/ทาวเฮาส์'), ('3', 'หอพัก/คอนโด/ห้องเช่า'), ('4', 'พักรวมกับคนจำนวนมาก'), ('5', 'อื่น ๆ (โปรดระบุข้อความ)')], default='-', max_length=100, null=True, verbose_name='ลักษณะที่พักอาศัย')),
                ('TypeLive_Other', models.CharField(blank=True, default='-', max_length=200, null=True, verbose_name='ระบุลักษะณะการพักอาศัย')),
                ('DatePatient', models.DateField(default=datetime.date.today, verbose_name='วันที่เริ่มป่วย')),
                ('DateFirstTreat', models.DateField(default=datetime.date.today, verbose_name='วันที่รักษาครั้งแรก')),
                ('DateDiagnose', models.DateField(default=datetime.date.today, verbose_name='วันที่วินิจฉัยโรค')),
                ('NameHospitalTreat', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='ชื่อสถานพยาบาลที่เข้ารักษาในปัจจุบัน')),
                ('HospitalProvince', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='สถานพยาบาลอยู่ในจังหวัด')),
                ('ShowSymptom', models.CharField(blank=True, choices=[('1', 'ไม่มีอาการใด ๆ'), ('2', 'มีอาการ แต่ไม่มีอาการระบบทางเดินหายใจ'), ('3', 'มีอาการระบบทางเดินหายใจ และระบุ O2Sat %')], default='-', max_length=200, null=True, verbose_name='อาการและอาการแสดง(ณ วันที่รายงาน)')),
                ('ShowSymptom_O2', models.CharField(blank=True, default='-', max_length=3, null=True, verbose_name='ค่า O2 Sat %')),
                ('TypeViolence', models.CharField(blank=True, choices=[('1', 'เป็นปอดอักเสบ'), ('2', 'ใส่เครื่องช่วยหายใจ'), ('3', 'เสียชีวิต')], default='-', max_length=100, null=True, verbose_name='ความรุนแรงของอาการ')),
                ('DiseasePatient', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='โรคประจำตัว')),
                ('CaseFemale', models.CharField(blank=True, choices=[('0', '-'), ('1', 'ไม่ตั้งครรภ์'), ('2', 'ตั้งครรภ์')], default='-', max_length=50, null=True, verbose_name='กรณีเพศหญิง')),
                ('DateCheckRTPCR', models.DateField(default=datetime.date.today, verbose_name='วันที่ตรวจ RT PCR')),
                ('TypeExampleRTPCR', models.CharField(blank=True, default='-', max_length=50, null=True, verbose_name='ชนิดตัวอย่าง')),
                ('PlaceCheckRTPCR', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='สถานที่ตรวจ')),
                ('ResultsCheckRTPCR', models.CharField(blank=True, choices=[('0', '-'), ('1', 'Detected'), ('2', 'Not Detected')], default='-', max_length=50, null=True, verbose_name='ผลการตรวจ RT PCR')),
                ('DateCheckAntigen', models.DateField(default=datetime.date.today, verbose_name='วันที่ตรวจ Antigen')),
                ('TypeExampleAntigen', models.CharField(blank=True, default='-', max_length=50, null=True, verbose_name='ชนิดตัวอย่าง')),
                ('PlaceCheckAntigen', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='สถานที่ตรวจ')),
                ('ResultsCheckAntigen', models.CharField(blank=True, choices=[('0', '-'), ('1', 'Detected'), ('2', 'Not Detected')], default='-', max_length=50, null=True, verbose_name='ผลการตรวจ Antigen')),
                ('DateCheckAntibody1', models.DateField(default=datetime.date.today, verbose_name='วันที่ตรวจ Antibody ครั้งที่ 1')),
                ('TypeExampleAntibody1', models.CharField(blank=True, default='-', max_length=50, null=True, verbose_name='ชนิดตัวอย่าง')),
                ('PlaceCheckAntibody1', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='สถานที่ตรวจ')),
                ('CheckAntibody1IgM', models.CharField(blank=True, default='-', max_length=10, null=True, verbose_name='Antibody ครั้งที่ 1 Igm')),
                ('CheckAntibody1IgG', models.CharField(blank=True, default='-', max_length=10, null=True, verbose_name='Antibody ครั้งที่ 1 IgG')),
                ('CheckAntibody1Neg', models.BooleanField(blank=True, default=False, null=True, verbose_name='มี')),
                ('DateCheckAntibody2', models.DateField(default=datetime.date.today, verbose_name='วันที่ตรวจ Antibody ครั้งที่ 2')),
                ('TypeExampleAntibody2', models.CharField(blank=True, default='-', max_length=50, null=True, verbose_name='ชนิดตัวอย่าง')),
                ('PlaceCheckAntibody2', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='สถานที่ตรวจ')),
                ('CheckAntibody2IgM', models.CharField(blank=True, default='-', max_length=10, null=True, verbose_name='Antibody ครั้งที่ 2 Igm')),
                ('CheckAntibody2IgG', models.CharField(blank=True, default='-', max_length=10, null=True, verbose_name='Antibody ครั้งที่ 2 IgG')),
                ('CheckAntibody2Neg', models.BooleanField(blank=True, default=False, null=True, verbose_name='มี')),
                ('ReceivedVaccine', models.BooleanField(blank=True, default=False, null=True, verbose_name='เคยรับวัคซีน')),
                ('BookReceivedVaccine', models.BooleanField(blank=True, default=False, null=True, verbose_name='จองวัคซีน')),
                ('DateReceivedVaccine1', models.DateField(default=datetime.date.today, verbose_name='วันที่ได้รับวัคซีน ครั้งที่ 1')),
                ('NameVaccine1', models.CharField(blank=True, choices=[('0', '-'), ('1', 'Sinovac'), ('2', 'Astra Zeneca'), ('2', 'Pfizer'), ('2', 'Moderna')], default='-', max_length=20, null=True, verbose_name='ชื่อวัคซีน')),
                ('PlaceReceivedVaccine1', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='สถานที่ฉีด')),
                ('DateReceivedVaccine2', models.DateField(default=datetime.date.today, verbose_name='วันที่ได้รับวัคซีน ครั้งที่ 2')),
                ('NameVaccine2', models.CharField(blank=True, choices=[('0', '-'), ('1', 'Sinovac'), ('2', 'Astra Zeneca'), ('2', 'Pfizer'), ('2', 'Moderna')], default='-', max_length=20, null=True, verbose_name='ชื่อวัคซีน')),
                ('PlaceReceivedVaccine2', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='สถานที่ฉีด')),
                ('LiveInCovid', models.BooleanField(blank=True, default=False, null=True, verbose_name='ที่อาศัยมีการระบาด COVID')),
                ('InThaiProvice', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='จังหวัด')),
                ('InForeignCountry', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='ประเทศ')),
                ('InForeignCity', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='เมือง')),
                ('NearCovid', models.BooleanField(blank=True, default=False, null=True, verbose_name='ได้ดูแลหรือสัมผัสใกล้ชิดกับผู้ป่วยอาการคล้ายไข้หวัดใหญ่หรือปลอดอักเสบ')),
                ('ContactCovid', models.BooleanField(blank=True, default=False, null=True, verbose_name='สัมผัสกับผู้ป่วยยืนยันโรคติดต่อเชื่อไวรัสโคโรนา 2019')),
                ('ContactCovidText', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='สัมผัสกับผู้ป่วยชื่อ')),
                ('CareerNearCovid', models.BooleanField(blank=True, default=False, null=True, verbose_name='ประกอบอาชีพที่สัมผัสใกล้ชิดกับนักท่องเทียวต่างชาติหรือแรงงานต่างชาติ')),
                ('TravelInCovid', models.BooleanField(blank=True, default=False, null=True, verbose_name='เดินทางไปในสถานที่หรือทำกิจกรรมที่มีคนหนาแน่นหรือพลุกพล่าน')),
                ('TravelInCovidText', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='ชื่อสถานที่')),
                ('AuthoritiesMedical', models.BooleanField(blank=True, default=False, null=True, verbose_name='เป็นบุคลากรทางการแพทย์และสาธารณะสุขหรือเจ้าหน้าที่ห้องปฏิบัติการ')),
                ('AuthoritiesMedicalCarePatient', models.BooleanField(blank=True, default=False, null=True, verbose_name='ดูแลหรือให้บริการผู้ป่วยโควิด 19 หรือ เป็นผู้เก็บ/นำส่ง/ตรวจตัวอย่างของผู้ติดเชื้อโควิด 19')),
                ('HistoryRisky', models.BooleanField(blank=True, default=False, null=True, verbose_name='มีประวัติเสี่ยงอื่น ๆ')),
                ('HistoryRiskyText', models.CharField(blank=True, default='-', max_length=200, null=True, verbose_name='ระบุประวัติเสี่ยงอื่น ๆ')),
                ('ContactRisky', models.IntegerField(blank=True, default=0, null=True, verbose_name='ผู้สัมผัสใหล้ชิดเสี่ยงสูงกี่คน')),
                ('ContactRiskyTrace', models.IntegerField(blank=True, default=0, null=True, verbose_name='ติดตามได้กี่คน')),
                ('PlaceConfineContactRisky1', models.IntegerField(blank=True, default=0, null=True, verbose_name='สถานที่กักตัว(ที่บ้าน)กี่คน')),
                ('PlaceConfineContactRisky2', models.IntegerField(blank=True, default=0, null=True, verbose_name='สถานที่กักตัว(สถานที่กักตัว)กี่คน')),
                ('ContactLowRisk', models.IntegerField(blank=True, default=0, null=True, verbose_name='ผู้สัมผัสใหล้ชิดเสี่ยงต่ำกี่คน')),
                ('ContactLowRiskTrace', models.IntegerField(blank=True, default=0, null=True, verbose_name='ติดตามได้กี่คน')),
                ('PlaceConfineContactLowRisk1', models.IntegerField(blank=True, default=0, null=True, verbose_name='สถานที่กักตัว(ที่บ้าน)กี่คน')),
                ('PlaceConfineContactLowRisk2', models.IntegerField(blank=True, default=0, null=True, verbose_name='สถานที่กักตัว(สถานที่กักตัว)กี่คน')),
                ('UserReport', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='ผู้รายงาน')),
                ('Unit', models.CharField(blank=True, max_length=100, null=True, verbose_name='หน่วยงาน')),
                ('Mobile2', models.CharField(blank=True, default='-', max_length=10, null=True, verbose_name='เบอร์โทรศัพท์ จนท.')),
                ('DateReport', models.DateField(default=datetime.date.today, verbose_name='วันที่')),
                ('Patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Patient_colona3', to='Patient.patient')),
            ],
            options={
                'verbose_name_plural': 'แบบฟอร์ม Corona3',
            },
        ),
    ]
