from datetime import date
import datetime
from re import T
from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

# from UserData.models import User
from Patient.models import Patient

class Corona3(models.Model):
    class Meta:
        verbose_name_plural = "แบบฟอร์ม Corona3"
    CHOICE_Province = (
        ('1',' กรุงเทพมหานคร'),
        ('2',' กระบี่ '),
        ('3',' กาญจนบุรี '),
        ('4',' กาฬสินธุ์ '),
        ('5',' กำแพงเพชร '),
        ('6',' ขอนแก่น '),
        ('7',' จันทบุรี '),
        ('8',' ฉะเชิงเทรา'),
        ('9',' ชลบุรี '),
        ('10',' ชัยนาท '),
        ('11',' ชัยภูมิ '),
        ('12',' ชุมพร '),
        ('13',' เชียงราย '),
        ('14',' เชียงใหม่ '),
        ('15',' ตรัง '),
        ('16',' ตราด '),
        ('17',' ตาก '),
        ('18',' นครนายก'),
        ('19',' นครปฐม '),
        ('20',' นครพนม '),
        ('21',' นครราชสีมา '),
        ('22',' นครศรีธรรมราช '),
        ('23',' นครสวรรค์ '),
        ('24',' นนทบุรี '),
        ('25',' นราธิวาส '),
        ('26',' น่าน '),
        ('27',' บึงกาฬ '),
        ('28',' บุรีรัมย์ '),
        ('29',' ปทุมธานี '),
        ('30',' ประจวบคีรีขันธ์ '),
        ('31',' ปราจีนบุรี '),
        ('32',' ปัตตานี '),
        ('33',' พระนครศรีอยุธยา '),
        ('34',' พังงา '),
        ('35',' พัทลุง '),
        ('36',' พิจิตร '),
        ('37',' พิษณุโลก '),
        ('38',' เพชรบุรี '),
        ('39',' เพชรบูรณ์ '),
        ('40',' แพร่ '),
        ('41',' พะเยา '),
        ('42',' ภูเก็ต '),
        ('43',' มหาสารคาม '),
        ('44',' มุกดาหาร '),
        ('45',' แม่ฮ่องสอน '),
        ('46',' ยะลา '),
        ('47',' ยโสธร '),
        ('48',' ร้อยเอ็ด '),
        ('49',' ระนอง '),
        ('50',' ระยอง '),
        ('51',' ราชบุรี '),
        ('52',' ลพบุรี '),
        ('53',' ลำปาง '),
        ('54',' ลำพูน '),
        ('55',' เลย '),
        ('56',' ศรีสะเกษ'),
        ('57',' สกลนคร '),
        ('58',' สงขลา '),
        ('59',' สตูล '),
        ('60',' สมุทรปราการ '),
        ('61',' สมุทรสงคราม '),
        ('62',' สมุทรสาคร '),
        ('63',' สระแก้ว '),
        ('64',' สระบุรี '),
        ('65',' สิงห์บุรี '),
        ('66',' สุโขทัย '),
        ('67',' สุพรรณบุรี '),
        ('68',' สุราษฎร์ธานี '),
        ('69',' สุรินทร์ '),
        ('70',' หนองคาย '),
        ('71',' หนองบัวลำภู '),
        ('72',' อ่างทอง '),
        ('73',' อุดรธานี '),
        ('74',' อุทัยธานี '),
        ('75',' อุตรดิตถ์ '),
        ('76',' อุบลราชธานี '),
        ('77',' อำนาจเจริญ'),
    )
                                    
    Patient = models.ForeignKey(
                                Patient,
                                on_delete = models.DO_NOTHING,
                                related_name = 'Patient_colona3',
                                blank = True, 
                                null = True,)
    PersonID = models.CharField(
                                max_length = 13,
                                unique = True,
                                blank = False, 
                                null = False,
                                verbose_name = 'เลขบัตรประชาชน/พาสปอร์ต')

    FullName = models.CharField(
                                max_length = 255,
                                blank = False, 
                                null = False,
                                verbose_name = 'ชื่อผู้ป่วย')
    CHOICE_Gender = (
        ( '-' ,  'ไม่ระบุ' ) ,
        ( 'ช' ,  'ชาย' ) ,
        ( 'ญ' ,  'หญิง' ) ,
    ) 
    Gender = models.CharField(
                                max_length = 8,
                                choices = CHOICE_Gender, 
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'เพศ')

    BirthYear  = models.IntegerField(
                                blank = False, 
                                null = False,
                                verbose_name = 'พ.ศ.เกิด')                                

    CHOICE_Nationority = (
        ( '0' ,  'ไม่ระบุ' ) ,
        ( '1' ,  'ไทย' ) ,
        ( '2' ,  'ลาว' ) ,
        ( '3' ,  'กัมพูชา' ) ,
        ( '4' ,  'พม่า' ) ,
        ( '5' ,  'จีน' ) ,
        ( '6' ,  'อินเดีย' ) ,
        ( '7' ,  'มาเลเซีย' ) ,
        ( '8' ,  'สิงค์โปร' ) ,
    ) 
    Nationality = models.CharField(
                                    max_length = 20,
                                    choices = CHOICE_Nationority, 
                                    default = '-', 
                                    null = True,
                                    blank = True,
                                    verbose_name = 'สัญชาติ')
    CHOICE_TypeCheck = (
        ( '1' ,  'PUI' ) ,
        ( '2' ,  'ผู้สัมผัสใกล้ชิด' ) ,
        ( '3' ,  'การค้นหาสำรวจเชิงรุก' ) ,
        ( '4' ,  'Sentinet Surevellence' ) ,
        ( '5' ,  'อื่น ๆ (โปรดระบุข้อความ)'),
    )
    TypeCheck = models.CharField(
                                max_length = 100,
                                choices = CHOICE_TypeCheck, 

                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ประเภทตรวจพบ')
    TypeCheck_Other = models.CharField(
                                    max_length = 200,
                                    default = '-', 
                                    null = False,
                                    blank = True,
                                    verbose_name = 'ระบุการตรวจพบจากกรณีอื่น ๆ')    
    CareerPatient = models.CharField(
                                    max_length = 3,
                                    default = "-",
                                    blank = True,
                                    null = True,
                                    verbose_name = 'อาชีพ(ระบุลักษณะงาน เช่น บุคลากรทางการแพทย์)' ) 
    PlaceWork = models.CharField(
                                max_length = 250,
                                default = '-',
                                null = True,
                                blank = True,
                                verbose_name = 'สถานที่ทำงาน/สถานศึกษา')
    Mobile  = models.CharField(
                                max_length = 20,
                                blank = False, 
                                null = False,
                                verbose_name = 'เบอร์มือถือ')
    Address = models.CharField(
                                max_length = 100,
                                default = None, 
                                verbose_name = 'ที่อยู่ปัจจุบัน', 
                                null = True, 
                                blank = True)
    Swine = models.IntegerField(
                                null = True,
                                blank = True,
                                verbose_name = 'หมู่ที่')
    SubDistrict = models.CharField(
                                max_length = 50,
                                default = None, 
                                verbose_name = 'ตำบล/แขวง', 
                                null = True, 
                                blank = True)
    District = models.CharField(
                                max_length = 50,
                                default = None, 
                                verbose_name = 'อำเภอ/เขต', 
                                null = True, 
                                blank = True)
    Province = models.CharField(
                                max_length = 50,
                                choices = CHOICE_Province,
                                default = None, 
                                verbose_name = 'จังหวัด', 
                                null = True, 
                                blank = True)
    ZipCode = models.CharField(max_length = 5,
                                default = '-',
                                verbose_name = 'รหัสไปรษณีย์',
                                null = True,
                                blank = True)
    CHOICE_TypeLive = (
        ( '1' ,  'บ้านเดี่ยว' ) ,
        ( '2' ,  'ตึกแถว/ทาวเฮาส์' ) ,
        ( '3' ,  'หอพัก/คอนโด/ห้องเช่า' ) ,
        ( '4' ,  'พักรวมกับคนจำนวนมาก' ) ,
        ( '5' ,  'อื่น ๆ (โปรดระบุข้อความ)'),
    )
    TypeLive = models.CharField(
                                max_length = 100,
                                choices = CHOICE_TypeLive, 
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ลักษณะที่พักอาศัย')
    TypeLive_Other = models.CharField(
                                    max_length = 200,
                                    default = '-', 
                                    null = True,
                                    blank = True,
                                    verbose_name = 'ระบุลักษะณะการพักอาศัย')

    DatePatient = models.DateField(
                            default=datetime.date.today, 
                            verbose_name = 'วันที่เริ่มป่วย')
    DateFirstTreat = models.DateField(
                            default=datetime.date.today, 
                            verbose_name = 'วันที่รักษาครั้งแรก')
    DateDiagnose = models.DateField(
                            default=datetime.date.today, 
                            verbose_name = 'วันที่วินิจฉัยโรค')
    NameHospitalTreat = models.CharField(
                                max_length = 200,
                                default = None, 
                                verbose_name = 'ชื่อสถานพยาบาลที่เข้ารักษาในปัจจุบัน', 
                                null = True, 
                                blank = True)
    HospitalProvince = models.CharField(
                                max_length = 50,
                                choices = CHOICE_Province,
                                default = '-', 
                                verbose_name = 'สถานพยาบาลอยู่ในจังหวัด', 
                                null = True, 
                                blank = True)
    CHOICE_ShowSymptom = (
        ( '1' ,  'ไม่มีอาการใด ๆ' ) ,
        ( '2' ,  'มีอาการ แต่ไม่มีอาการระบบทางเดินหายใจ' ) ,
        ( '3' ,  'มีอาการระบบทางเดินหายใจ และระบุ O2Sat %' ) ,
    )
    ShowSymptom = models.CharField(
                                max_length = 200,
                                choices = CHOICE_ShowSymptom, 
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'อาการและอาการแสดง(ณ วันที่รายงาน)')
    ShowSymptom_O2 = models.CharField(
                                    max_length = 3,
                                    default = '-', 
                                    null = True,
                                    blank = True,
                                    verbose_name = 'ค่า O2 Sat %')
    CHOICE_TypeViolence = (
        ( '1' ,  'เป็นปอดอักเสบ' ) ,
        ( '2' ,  'ใส่เครื่องช่วยหายใจ' ) ,
        ( '3' ,  'เสียชีวิต' ) ,
    )
    TypeViolence = models.CharField(
                                max_length = 20,
                                choices = CHOICE_TypeViolence, 
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ความรุนแรงของอาการ')
    DiseasePatient = models.CharField(
                                max_length = 100,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'โรคประจำตัว')
    CHOICE_CaseFemale = (
        ( '0' ,  '-' ) ,
        ( '1' ,  'ไม่ตั้งครรภ์' ) ,
        ( '2' ,  'ตั้งครรภ์' ) ,
    )
    CaseFemale = models.CharField(
                                max_length = 15,
                                choices = CHOICE_CaseFemale, 
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'กรณีเพศหญิง')


    DateCheckRTPCR = models.DateField(
                            default=datetime.date.today, 
                            verbose_name = 'วันที่ตรวจ RT PCR')

    TypeExampleRTPCR = models.CharField(
                                max_length = 50,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ชนิดตัวอย่าง')
    PlaceCheckRTPCR = models.CharField(
                                max_length = 100,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'สถานที่ตรวจ')
    CHOICE_ResultsCheck = (
        ( '0' ,  '-' ) ,
        ( '1' ,  'Detected' ) ,
        ( '2' ,  'Not Detected' ) ,
    )
    ResultsCheckRTPCR = models.CharField(
                                max_length = 50,
                                choices = CHOICE_ResultsCheck, 
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ผลการตรวจ RT PCR')


    DateCheckAntigen = models.DateField(
                            default=datetime.date.today, 
                            verbose_name = 'วันที่ตรวจ Antigen')
    TypeExampleAntigen = models.CharField(
                                max_length = 50,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ชนิดตัวอย่าง')
    PlaceCheckAntigen = models.CharField(
                                max_length = 100,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'สถานที่ตรวจ')
    
    ResultsCheckAntigen = models.CharField(
                                max_length = 50,
                                choices = CHOICE_ResultsCheck, 
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ผลการตรวจ Antigen')
    


    DateCheckAntibody1 = models.DateField(
                            default=datetime.date.today, 
                                null = True,
                                blank = True,                            
                            verbose_name = 'วันที่ตรวจ Antibody ครั้งที่ 1')
    TypeExampleAntibody1 = models.CharField(
                                max_length = 50,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ชนิดตัวอย่าง')
    PlaceCheckAntibody1 = models.CharField(
                                max_length = 100,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'สถานที่ตรวจ')
    CheckAntibody1IgM = models.CharField(
                                max_length = 10,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'Antibody ครั้งที่ 1 Igm')
    CheckAntibody1IgG = models.CharField(
                                max_length = 10,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'Antibody ครั้งที่ 1 IgG')
    CheckAntibody1Neg = models.CharField(
                                    max_length = 10,
                                    default='-',
                                    verbose_name= "Antibody ครั้งที่ 1 Neg",
                                    blank = True, 
                                    null = True,)


    DateCheckAntibody2 = models.DateField(
                            default=datetime.date.today, 
                                null = True,
                                blank = True,                            
                            verbose_name = 'วันที่ตรวจ Antibody ครั้งที่ 2')
    TypeExampleAntibody2 = models.CharField(
                                max_length = 50,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ชนิดตัวอย่าง')
    PlaceCheckAntibody2 = models.CharField(
                                max_length = 100,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'สถานที่ตรวจ')
    CheckAntibody2IgM = models.CharField(
                                max_length = 10,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'Antibody ครั้งที่ 2 Igm')
    CheckAntibody2IgG = models.CharField(
                                max_length = 10,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'Antibody ครั้งที่ 2 IgG')
    CheckAntibody2Neg = models.CharField(
                                    max_length = 10,
                                    default='-',
                                    verbose_name= "Anitibody ครั้งที่ 2 Neg",
                                    blank = True, 
                                    null = True,)
    
    ReceivedVaccine = BooleanField(
                                    default = False, 
                                    verbose_name= "เคยรับวัคซีน",
                                    blank = True, 
                                    null = True,)
    
    BookReceivedVaccine = BooleanField(
                                    default = False, 
                                    verbose_name= "จองวัคซีน",
                                    blank = True, 
                                    null = True,)
    
    DateReceivedVaccine1 = models.DateField(
                                default=datetime.date.today, 
                                null = True,
                                blank = True,                            
                                verbose_name = 'วันที่ได้รับวัคซีน ครั้งที่ 1')
    CHOICE_NameVaccine = (
        ( '0' ,  '-' ) ,
        ( '1' ,  'Sinovac' ) ,
        ( '2' ,  'Astra Zeneca' ) ,
        ( '2' ,  'Pfizer' ) ,
        ( '2' ,  'Moderna' ) ,
    )
    NameVaccine1 = models.CharField(
                                max_length = 20,
                                choices = CHOICE_NameVaccine, 
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ชื่อวัคซีน')
    PlaceReceivedVaccine1 = models.CharField(
                                max_length = 100,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'สถานที่ฉีด')
    
    DateReceivedVaccine2 = models.DateField(
                            default=datetime.date.today, 
                                null = True,
                                blank = True,                            
                            verbose_name = 'วันที่ได้รับวัคซีน ครั้งที่ 2')
    NameVaccine2 = models.CharField(
                                max_length = 20,
                                choices = CHOICE_NameVaccine, 
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ชื่อวัคซีน')
    PlaceReceivedVaccine2 = models.CharField(
                                max_length = 100,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'สถานที่ฉีด')

    LiveInCovid = BooleanField(
                                    default = False, 
                                    verbose_name = "ที่อาศัยมีการระบาด COVID",
                                    blank = True, 
                                    null = True,)
                                       
    InThaiProvince = models.CharField(
                                        max_length = 100,
                                        choices = CHOICE_Province, 
                                        default = '-', 
                                        null = True,
                                        blank = True,
                                        verbose_name = 'จังหวัด')
    # InThaiProvice = models.CharField(
    #                             max_length = 100,
    #                             default = '-', 
    #                             null = True,
    #                             blank = True,
    #                             verbose_name = 'จังหวัด')
    InForeignCountry = models.CharField(
                                max_length = 100,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = '14 วันก่อนอาศัยอยู่ประเทศ')
    
    InForeignCity = models.CharField(
                                max_length = 100,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = '14 วันก่อนอาศัยอยู่เมือง')
    NearCovid = BooleanField(
                                    default = False, 
                                    verbose_name= "ได้ดูแลหรือสัมผัสใกล้ชิดกับผู้ป่วยอาการคล้ายไข้หวัดใหญ่หรือปลอดอักเสบ",
                                    blank = True, 
                                    null = True,)
    ContactCovid = BooleanField(
                                    default = False, 
                                    verbose_name= "มีประวัติสัมผัสกับผู้ป่วยยืนยันโรคติดต่อเชื่อไวรัสโคโรนา 2019",
                                    blank = True, 
                                    null = True,)
    ContactCovidText = models.CharField(
                                max_length = 100,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'สัมผัสกับผู้ป่วยชื่อ')
    CareerNearCovid = BooleanField(
                                    default = False, 
                                    verbose_name= "ประกอบอาชีพที่สัมผัสใกล้ชิด กับนักท่องเทียวต่างชาติ หรือแรงงานต่างชาติ",
                                    blank = True, 
                                    null = True,)
    
    TravelInCovid = BooleanField(
                                    default = False, 
                                    verbose_name= "เดินทางไปในสถานที่ หรือทำกิจกรรมที่มีคนหนาแน่นหรือ พลุกพล่าน",
                                    blank = True, 
                                    null = True,)
    TravelInCovidText = models.CharField(
                                max_length = 100,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ชื่อสถานที่')
    AuthoritiesMedical = BooleanField(
                                    default = False, 
                                    verbose_name= "เป็นบุคลากรทางการแพทย์และสาธารณะสุขหรือเจ้าหน้าที่ห้องปฏิบัติการ",
                                    blank = True, 
                                    null = True,)
  
    AuthoritiesMedicalCarePatient = BooleanField(
                                    default = False, 
                                    verbose_name= "ดูแลหรือให้บริการผู้ป่วยโควิด 19 หรือ เป็นผู้เก็บ/นำส่ง/ตรวจตัวอย่างของผู้ติดเชื้อโควิด 19",
                                    blank = True, 
                                    null = True,)
    HistoryRisky = BooleanField(
                                    default = False, 
                                    verbose_name= "มีประวัติเสี่ยงอื่น ๆ",
                                    blank = True, 
                                    null = True,)
    HistoryRiskyText = models.CharField(
                                max_length = 200,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ระบุประวัติเสี่ยงอื่น ๆ')
    ContactRisky = models.IntegerField(
                                    default = 0, 
                                    verbose_name = 'ผู้สัมผัสใกล้ชิดเสี่ยงสูงกี่คน', 
                                    null = True,
                                    blank = True)
                    
    ContactRiskyTrace = models.IntegerField(
                                    default = 0, 
                                    verbose_name = 'ติดตามได้กี่คน', 
                                    null = True,
                                    blank = True)
    PlaceConfineContactRisky1 = models.IntegerField(
                                    default = 0, 
                                    verbose_name = 'สถานที่กักตัว(ที่บ้าน)กี่คน', 
                                    null = True,
                                    blank = True)
    PlaceConfineContactRisky2 = models.IntegerField(
                                    default = 0, 
                                    verbose_name = 'สถานที่กักตัว(สถานที่กักตัว)กี่คน', 
                                    null = True,
                                    blank = True)
    ContactLowRisk = models.IntegerField(
                                    default = 0, 
                                    verbose_name = 'ผู้สัมผัสใกล้ชิดเสี่ยงต่ำกี่คน', 
                                    null = True,
                                    blank = True)
                    
    ContactLowRiskTrace = models.IntegerField(
                                    default = 0, 
                                    verbose_name = 'ติดตามได้กี่คน', 
                                    null = True,
                                    blank = True)
    PlaceConfineContactLowRisk1 = models.IntegerField(
                                    default = 0, 
                                    verbose_name = 'สถานที่กักตัว(ที่บ้าน)กี่คน', 
                                    null = True,
                                    blank = True)
    PlaceConfineContactLowRisk2 = models.IntegerField(
                                    default = 0, 
                                    verbose_name = 'สถานที่กักตัว(สถานที่กักตัว)กี่คน', 
                                    null = True,
                                    blank = True)

    # class Meta:
    #         verbose_name_plural = "เจ้าหน้าที่รายงาน"

    UserReport = models.CharField(
                                max_length = 100,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'ผู้รายงาน')
    # UserReport = models.ForeignKey(
    #                                 on_delete=models.DO_NOTHING, 
    #                                 related_name='Corona3_User', 
    #                                 verbose_name = 'ผู้บันทึกข้อมูล')
    Unit = models.CharField(
                                max_length = 100,
                                null = True,
                                blank = True,
                                verbose_name = 'หน่วยงาน')
    Mobile2 = models.CharField(
                                max_length = 10,
                                default = '-', 
                                null = True,
                                blank = True,
                                verbose_name = 'เบอร์โทรศัพท์ จนท.')
    DateReport = models.DateField(
                                default=datetime.date.today, 
                                verbose_name = 'วันที่')



    @property
    def IsPersonID(self):
        if self.PersonID:
            return len(self.PersonID) == 13
        else:
            return False
            
    @property
    def Age(self):
        if self.BirthYear:
            today = date.today()
            return (today.year+543) - self.BirthYear
        else:
            return "-"

    @property
    def TypeCheck5(self):
        if self.TypeCheck == 5:
            self.TypeCheck_Other.null = True
            return self.TypeCheck_Other
        

    def __str__(self):
        return self.FullName
