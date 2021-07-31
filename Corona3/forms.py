from django import forms
from django.forms import ModelForm
from Corona3.models import Corona3

class BasicDataForm(ModelForm):
    class Meta:
        model = Corona3
        fields = [  'PersonID',
                    'FullName',
                    'Gender',
                    'BirthYear',
                    'Nationality',
                    'TypeCheck',
                    'TypeCheck_Other',
                    'CareerPatient',
                    'PlaceWork',
                    'Mobile',
                    'Address',
                    'Swine',
                    'SubDistrict',
                    'District',
                    'Province',
                    'ZipCode',
                    'TypeLive',
                    'TypeLive_Other',
                    'DatePatient',
                    'DateFirstTreat',
                    'DateDiagnose',
                    'NameHospitalTreat',
                    'HospitalProvince',
                    'ShowSymptom',
                    'ShowSymptom_O2',
                    'TypeViolence',
                    'DiseasePatient',
                    'CaseFemale',
                    'DateCheckRTPCR',
                    'TypeExampleRTPCR',
                    'PlaceCheckRTPCR',
                    'ResultsCheckRTPCR',
                    'DateCheckAntigen',
                    'TypeExampleAntigen',
                    'PlaceCheckAntigen',
                    'ResultsCheckAntigen',
                    'DateCheckAntibody1',
                    'TypeExampleAntibody1',
                    'PlaceCheckAntibody1',
                    'CheckAntibody1IgM',
                    'CheckAntibody1IgG',
                    'CheckAntibody1Neg',
                    'DateCheckAntibody2',
                    'TypeExampleAntibody2',
                    'PlaceCheckAntibody2',
                    'CheckAntibody2IgM',
                    'CheckAntibody2IgG',
                    'CheckAntibody2Neg',
                    'ReceivedVaccine',
                    'BookReceivedVaccine',
                    'DateReceivedVaccine1',
                    'NameVaccine1',
                    'PlaceReceivedVaccine1',
                    'DateReceivedVaccine2',
                    'NameVaccine2',
                    'PlaceReceivedVaccine2',
                    'InThaiProvince',
                    'InForeignCountry',
                    'InForeignCity',
                    'NearCovid',
                    'ContactCovid',
                    'ContactCovidText',
                    'CareerNearCovid',
                    'TravelInCovid',
                    'TravelInCovidText',
                    'AuthoritiesMedical',
                    'AuthoritiesMedicalCarePatient',
                    'HistoryRisky',
                    'HistoryRiskyText',
                    'ContactRisky',
                    'ContactRiskyTrace',
                    'PlaceConfineContactRisky1',
                    'PlaceConfineContactRisky2',
                    'ContactLowRisk',
                    'ContactLowRiskTrace',
                    'PlaceConfineContactLowRisk1',
                    'PlaceConfineContactLowRisk2',                    
                    'DateReport'
        ]

        widgets = {
            'PersonID': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': 'เลขบัตรประชาชน/พาสปอร์ต (จำเป็น)',
                        }),             
            'FullName': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': 'คำนำหน้า ชื่อ นามสกุล (จำเป็น)',
                        }),        
            'BirthYear': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),        
                             
            'Nationality': forms.Select(
                    attrs={'class': 'form-control', 
                        }),             
                             
            'TypeCheck': forms.Select(
                    attrs={'class': 'form-control', 
                        }),        
            'TypeCheck_Other': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                                
            'CareerPatient': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                                
            'PlaceWork': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                                
            'Gender': forms.Select(
                    attrs={'class': 'form-control', 
                        }),       
            'Mobile': forms.TextInput(
                    attrs={'class': 'form-control',
                    'placeholder': 'เบอร์มือถือ (จำเป็น)',
                        }),  
            'Address': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                                                      
            'Swine': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                                                      
            'SubDistrict': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                                                      
            'District': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                                                      
            'Province': forms.Select(
                    attrs={'class': 'form-control'
                        }),                                                      
            'ZipCode': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),            
            'TypeLive': forms.Select(
                    attrs={'class': 'form-control', 
                        }),                                                                        
            'TypeLive_Other': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                                                      
            'DatePatient': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'DiseasePatient': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'DateFirstTreat': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'DateDiagnose': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'NameHospitalTreat': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'HospitalProvince':forms.Select(
                    attrs={'class': 'form-control'
                        }),  
            'ShowSymptom': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'ShowSymptom_O2': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'TypeViolence': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'DiseasePatient': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'DateCheckRTPCR': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'TypeExampleRTPCR': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'PlaceCheckRTPCR': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'ResultsCheckRTPCR': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'DateCheckAntigen': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'TypeExampleAntigen': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'PlaceCheckAntigen': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'ResultsCheckAntigen': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'DateCheckAntibody1': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'TypeExampleAntibody1': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'PlaceCheckAntibody1': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'CheckAntibody1IgM': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'CheckAntibody1IgG': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'CheckAntibody1Neg': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'DateCheckAntibody2': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'TypeExampleAntibody2': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'PlaceCheckAntibody2': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'CheckAntibody2IgM': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'CheckAntibody2IgG': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),
            'CheckAntibody2Neg': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),     
            'CaseFemale': forms.Select(
                    attrs={'class': 'form-control', 
                        }),                                                    
            'TypeLive': forms.Select(
                    attrs={'class': 'form-control', 
                        }),                             
      
            'ReceivedVaccine': forms.CheckboxInput(attrs={'class': 'form-control',}),                          
            'BookReceivedVaccine': forms.CheckboxInput(
                                        attrs={'class': 'form-control',}
                                    ),                          
                                                 
                                           
            'DateReceivedVaccine1': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'PlaceReceivedVaccine1': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                         
            'NameVaccine1': forms.Select(
                    attrs={'class': 'form-control', 
                        }),  
            'DateReceivedVaccine2': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'PlaceReceivedVaccine2': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                         
            'InThaiProvince': forms.Select(
                    attrs={'class': 'form-control'
                        }),                         
            'InForeignCountry': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                         
            'InForeignCity': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                         
                        
            'NameVaccine2': forms.Select(
                    attrs={'class': 'form-control', 
                        }),  
            'NearCovid': forms.Select(
                    attrs={'class': 'form-control', 
                        }),  
            'ContactCovid': forms.Select(
                    attrs={'class': 'form-control', 
                        }),  
            'NameVaccine2': forms.Select(
                    attrs={'class': 'form-control', 
                        }),  
            'ContactCovidText': forms.TextInput(
                    attrs={'class': 'form-control'
                        }), 
            'CareerNearCovid': forms.CheckboxInput(attrs={'class': 'form-control',}),                          
            'TravelInCovid': forms.CheckboxInput(
                                        attrs={'class': 'form-control',}
                                    ),                          
            'TravelInCovidText': forms.TextInput(
                    attrs={'class': 'form-control'
                        }), 
            'AuthoritiesMedical': forms.CheckboxInput(attrs={'class': 'form-control',}),                          
            'AuthoritiesMedicalCarePatient': forms.CheckboxInput(
                                        attrs={'class': 'form-control',}
                                    ),                          
                                        
            'HistoryRisky': forms.CheckboxInput(
                                        attrs={'class': 'form-control',}
                                    ),                          
            'HistoryRiskyText': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),       
            'ContactRisky': forms.NumberInput(
                    attrs={'class': 'form-control'
                        }),             
            'ContactLowRisk': forms.NumberInput(
                    attrs={'class': 'form-control'
                        }),             
            'ContactLowRiskTrace': forms.NumberInput(
                    attrs={'class': 'form-control'
                        }),             
            'PlaceConfineContactRisky2': forms.NumberInput(
                    attrs={'class': 'form-control'
                        }),             
            'PlaceConfineContactRisky1': forms.NumberInput(
                    attrs={'class': 'form-control'
                        }),             
            'ContactRiskyTrace': forms.NumberInput(
                    attrs={'class': 'form-control'
                        }),             
            'PlaceConfineContactLowRisk1': forms.NumberInput(
                    attrs={'class': 'form-control'
                        }),             
            'PlaceConfineContactLowRisk2': forms.NumberInput(
                    attrs={'class': 'form-control'
                        }),             

            'DateReport': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        })
        }

    # def clean_PersonID(self):
    #     return self.cleaned_data['PersonID'] or None
class minDataForm(ModelForm):
    class Meta:
        model = Corona3
        fields = [  'PersonID',
                    'FullName',
                    'Gender',
                    'BirthYear',
                    'Nationality',
                    'CareerPatient',
                    'PlaceWork',
                    'TreatPlaceWork',
                    'Mobile',
                    'Address',
                    'DatePatient',
                    'DiseasePatient',
<<<<<<< HEAD
                    'CaseFemale',                   
                    'GoogleMap',
                    'Religion',
                    'BloodType',
                    'RightMedicalTreatment',
                    'Email',
                    'AirforceType',
                    'MobileRelative',
                    'CurrentStatus',
                    'ATK',
                    'PCR',
                    'VaccineDetail',
                    'HomeIsolation',
                    'LiveWith',
                    'DrugAllergyHistory',
                    'Symptom',
                    'Note'
=======
                    'CaseFemale',
                    'ReceivedVaccine',
                    'BookReceivedVaccine',
                    'DateReceivedVaccine1',
                    'NameVaccine1',
                    'PlaceReceivedVaccine1',
                    'DateReceivedVaccine2',
                    'NameVaccine2',
                    'PlaceReceivedVaccine2',
                    'InForeignCountry',
                    'InForeignCity',
                    'NearCovid',
                    'ContactCovid',
                    'ContactCovidText',
                    'CareerNearCovid',
                    'TravelInCovid',
                    'TravelInCovidText',
                    'AuthoritiesMedical',
                    'AuthoritiesMedicalCarePatient',
                    'HistoryRisky',
                    'HistoryRiskyText',
                    'ContactRisky',
                    'ContactRiskyTrace',
                    'PlaceConfineContactRisky1',
                    'PlaceConfineContactRisky2',
                    'ContactLowRisk',
                    'ContactLowRiskTrace',
                    'PlaceConfineContactLowRisk1',
                    'PlaceConfineContactLowRisk2',                    
                    'DateReport'
>>>>>>> DevMuek
        ]

        widgets = {
            'GoogleMap': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),  
            'Religion': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),  
            'BloodType': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),  
            'RightMedicalTreatment': forms.Select(
                    attrs={'class': 'form-control'
                        }),  
            'Email': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),    
            'AirforceType': forms.Select(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),    
            'MobileRelative': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),
            'CurrentStatus': forms.Select(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),           
            'ATK': forms.FileInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),
            'PCR': forms.FileInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),     
            'VaccineDetail': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),  
            'HomeIsolation': forms.Select(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),
            'LiveWith': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),        
            'DrugAllergyHistory': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),        
            'Symptom': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),        
            'Note': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),                                                          
            'PersonID': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),             
            'FullName': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': '',
                        }),        
            'BirthYear': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),        
                             
            'Nationality': forms.Select(
                    attrs={'class': 'form-control'
                        }),                                                 
            'CareerPatient': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                                
            'PlaceWork': forms.TextInput(
                    attrs={'class': 'form-control'
                        }), 
            'TreatPlaceWork': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),                                   
            'Gender': forms.Select(
                    attrs={'class': 'form-control', 
                        }),       
            'Mobile': forms.TextInput(
                    attrs={'class': 'form-control',
                    'placeholder': 'เบอร์มือถือ (จำเป็น)',
                        }),  
            'Address': forms.TextInput(
                    attrs={'class': 'form-control',
                        'placeholder': 'บ้านเลขที่ หมู่ ถนน ตำบล อำเภอ จังหวัด',
                        }),                                                    
            'DatePatient': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'DiseasePatient': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),         
            'CaseFemale': forms.Select(
                    attrs={'class': 'form-control', 
                        })
        }
