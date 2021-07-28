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
                    'DiseasePatient',
                    'CaseFemale',
                    'ReceivedVaccine',
                    'BookReceivedVaccine',
                    'DateReceivedVaccine1',
                    'NameVaccine1',
                    'PlaceReceivedVaccine1',
                    'DateReceivedVaccine2',
                    'NameVaccine2',
                    'PlaceReceivedVaccine2',
                    'InThaiProvice',
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
            'Province': forms.TextInput(
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
            'InThaiProvice': forms.TextInput(
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
    #         'FullName': forms.TextInput(
    #                 attrs={'class': 'form-control', 
    #                     'placeholder': 'คำนำหน้า ชื่อ นามสกุล',
    #                     })', 
    #         'Gender': forms.Select(
    #                 attrs={'class': 'form-control', 
    #                     })',      
    #         'BirthDay': forms.DateInput(
    #                 format=('%Y-%m-%d')',
    #                 attrs={'class': 'form-control', 
    #                     'placeholder': 'Select a date',
    #                     'type': 'date'
    #                     })',   
    #         'PersonID': forms.TextInput(
    #                 attrs={'class': 'form-control', 
    #                     'placeholder': 'เลขบัตรประชาชน',
    #                     })',          
    #         'Office': forms.Textarea(
    #                 attrs={'class': 'form-control', 
    #                     'rows': 3',
    #                     'cols': 40
    #                     })',
    #         'IsAirforce': forms.CheckboxInput(attrs={'class': 'form-control',})',                          
    
    #         'Mobile': forms.TextInput(
    #                 attrs={'class': 'form-control', 
    #                     'placeholder': 'เบอร์มือถือ',
    #                     })',   
    #         'Address': forms.Textarea(
    #                 attrs={'class': 'form-control', 
    #                     'rows': 3',
    #                     'cols': 40
    #                     })',     
    #         'EmergencyMobile': forms.TextInput(
    #                 attrs={'class': 'form-control', 
    #                     'placeholder': 'เบอร์มือถือ',
    #                     })',                                                                                                                                          
                                                                                                                
    #         'Comment': forms.Textarea(
    #                 attrs={'class': 'form-control', 
    #                     'rows': 3',
    #                     })',    
    #         'IsAMED': forms.CheckboxInput(attrs={'class': 'form-control',})',                          
                            
    #         'CurrentStatus': forms.Select(
    #                 attrs={'class': 'form-control', 
    #                     })',   
    #         'CurrentTreatment': forms.Select(
    #                 attrs={'class': 'form-control', 
    #                     })',                                                                                                                                                                     
    #     }

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
                    'DiseasePatient',
                    'CaseFemale',
                    'ReceivedVaccine',
                    'BookReceivedVaccine',
                    'DateReceivedVaccine1',
                    'NameVaccine1',
                    'PlaceReceivedVaccine1',
                    'DateReceivedVaccine2',
                    'NameVaccine2',
                    'PlaceReceivedVaccine2',
                    'InThaiProvice',
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
                    attrs={'class': 'form-control',
                        'placeholder': 'บ้านเลขที่ หมู่ ถนน ตำบล อำเภอ จังหวัด',
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
            'Province': forms.TextInput(
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
            'InThaiProvice': forms.TextInput(
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
