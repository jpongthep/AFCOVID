from django import forms
from django.forms import ModelForm

from Corona3.models import Corona3

class Corona3BasicDataForm(ModelForm):
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
                    'ShowSymptom',
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
                        'placeholder': 'เลขบัตรประชาชน/พาสปอร์ต',
                        }),             
            'FullName': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': 'คำนำหน้า ชื่อ นามสกุล',
                        }),        
            'BirthYear': forms.TextInput(
                    attrs={'class': 'form-control'
                        }),        
                             
            'Nationality': forms.Select(
                    attrs={'class': 'form-control', 
                        }),             
            'Gender': forms.Select(
                    attrs={'class': 'form-control', 
                        }),             
            'DatePatient': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'DateReceivedVaccine1': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),

            'DateReceivedVaccine2': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
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

