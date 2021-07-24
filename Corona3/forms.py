from django.db import models
from django import forms
from django.forms import ModelForm

from Corona3.models import Corona3
# , StatusLog, TreatmentLog

class Corona3BasicDataForm(ModelForm):
    class Meta:
        model = Corona3
        fields = [
                    'Patient', 
                    'FullName',
                    'Gender',  
                    'AgePaient', 
                    'Nationality', 
                    'TypeCheck', 
                    'TypeCheck_Other',
                    'CareerPatient', 
                    'PlaceWork', 
                    'Mobile', 
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
                    'LiveInCovid',
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
                    'UserReport',
                    'Unit',
                    'MobileTel',
                    'DateReport',

                ]
        exclude = [                    
                    'Patient',
        ]
        widgets = {
            'DatePatient': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
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
            'DateCheckRTPCR': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'DateCheckAntigen': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'DateCheckAntibody1': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'DateCheckAntibody2': forms.DateInput(
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
                        }),
            'FullName': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': 'คำนำหน้า ชื่อ นามสกุล',
                        }),
            'Gender': forms.Select(
                    attrs={'class': 'form-control', 
                        }),      
            'Patient': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': 'เลขบัตรประชาชน',
                        }),          
            # 'Office': forms.Textarea(
            #         attrs={'class': 'form-control', 
            #             'rows': 3,
            #             'cols': 40
            #             }),
            'Mobile': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': 'เบอร์มือถือ',
                        }),   
            'MobileTel': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': 'เบอร์มือถือ',
                        }),   
            # 'Address': forms.Textarea(
            #         attrs={'class': 'form-control', 
            #             'rows': 3,
            #             'cols': 40
            #             }),     
            # 'EmergencyMobile': forms.TextInput(
            #         attrs={'class': 'form-control', 
            #             'placeholder': 'เบอร์มือถือ',
            #             }),                                                                                                                                          
                                                                                                                
            # 'Comment': forms.Textarea(
            #         attrs={'class': 'form-control', 
            #             'rows': 3,
            #             }),                                                                                                                      
        }


# class PatientCOVIDForm(PatientBasicDataForm):

#     def __init__(self, *args, **kwargs):
#         super(PatientBasicDataForm, self).__init__(*args, **kwargs)
#         self.fields['DatePositive'].widget = forms.DateInput(
#                                                 format=('%Y-%m-%d'),
#                                                 attrs={'class': 'form-control', 
#                                                     'placeholder': 'Select a date',
#                                                     'type': 'date'
#                                                     })
#         self.fields['InfectiousName'].widget = forms.Select(
#                                                 attrs={'class': 'form-control', 
#                                                     })
#         self.fields['Corona3'].widget = forms.FileInput(attrs={'class': 'form-control'})
#         self.fields['DetectedResult'].widget = forms.FileInput(attrs={'class': 'form-control'})
#         self.fields['ConfirmedPatient'].widget = forms.CheckboxInput(attrs={'class': 'form-control',})
        
#     class Meta(PatientBasicDataForm.Meta):
#         fields = PatientBasicDataForm.Meta.fields + [
#                     'DatePositive',
#                     'InfectiousName',
#                     'Corona3',
#                     'DetectedResult',
#                     'ConfirmedPatient',                    
#                 ]
#         exclude = PatientBasicDataForm.Meta.exclude + [                    
#                     'ConfirmUser',
#                 ]

           

# class PatientForm(PatientBasicDataForm):

#     def __init__(self, *args, **kwargs):
#         super(PatientBasicDataForm, self).__init__(*args, **kwargs)
#         self.fields['EmergencyMobile'].widget.attrs['class'] = 'form-control'

#     class Meta(PatientBasicDataForm.Meta):
#         model = Patient
#         fields = '__all__'
#         exclude = ('DataUser','ConfirmUser','ConfirmedPatient', )
#         fields = '__all__'         
#         exclude = (                    
#                     'DataUser',
#                     'ConfirmUser',
#                     'ConfirmedPatient',
#                     'CurrentStatus', 
#                     'CurrentTreatment',
#         )      
          


class StatusLogForm(ModelForm):
        pass
#     class Meta:
#         model = StatusLog
#         fields = ('Date', 'Status', 'Comment')
#         # exclude = ('ThePatient','RecorderUser')
#         widgets = {
#             'Date': forms.DateInput(
#                     format=('%Y-%m-%d'),
#                     attrs={'class': 'form-control', 
#                         'placeholder': 'Select a date',
#                         'type': 'date'
#                         }),
#             'Status': forms.Select(
#                     attrs={'class': 'form-control', 
#                         }),
#             'Comment': forms.Textarea(
#                     attrs={'class': 'form-control', 
#                         'rows': 3,
#                         }), 
#         }

class TreatmentLogForm(ModelForm):
    pass
#     class Meta:
#         model = TreatmentLog
#         fields = ('Date', 'Treatment', 'Comment')
#         # exclude = ('ThePatient','RecorderUser')

#         widgets = {
#             'Date': forms.DateInput(
#                     format=('%Y-%m-%d'),
#                     attrs={'class': 'form-control', 
#                         'placeholder': 'Select a date',
#                         'type': 'date'
#                         }) ,
#             'Treatment': forms.Select(
#                     attrs={'class': 'form-control', 
#                         }),
#             'Comment': forms.Textarea(
#                     attrs={'class': 'form-control', 
#                         'rows': 3,
#                         }), 
#         }
