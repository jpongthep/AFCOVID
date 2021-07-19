from django.db import models
from django import forms
from django.forms import ModelForm

from Patient.models import Patient, StatusLog, TreatmentLog

class PatientBasicDataForm(ModelForm):
    class Meta:
        model = Patient
        fields = [
                    'Date', 
                    'DataUser', 
                    'FullName',
                    'Gender',  
                    'BirthDay', 
                    'PersonID', 
                    'Office', 
                    'IsAirforce',
                    'Mobile', 
                    'Address', 
                    'EmergencyMobile', 
                    'Comment',
                ]
        exclude = [                    
                    'DataUser',
        ]
        widgets = {
            'Date': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'FullName': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': 'คำนำหน้า ชื่อ นามสกุล',
                        }),
            # 'InfectiousName': forms.Select(
            #         attrs={'class': 'form-control', 
            #             'placeholder': 'ผู้ติดเชื้อที่ใกล้ชิด',
            #             }),     
            'Gender': forms.Select(
                    attrs={'class': 'form-control', 
                        }),      
            'BirthDay': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),   
            'PersonID': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': 'เลขบัตรประชาชน',
                        }),          
            'Office': forms.Textarea(
                    attrs={'class': 'form-control', 
                        'rows': 3,
                        'cols': 40
                        }),
            'IsAirforce': forms.CheckboxInput(attrs={'class': 'form-control',}),                          
            # 'DatePositive': forms.DateInput(
            #         format=('%Y-%m-%d'),
            #         attrs={'class': 'form-control', 
            #             'placeholder': 'Select a date',
            #             'type': 'date'
            #             }),       
            'Mobile': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': 'เบอร์มือถือ',
                        }),   
            'Address': forms.Textarea(
                    attrs={'class': 'form-control', 
                        'rows': 3,
                        'cols': 40
                        }),     
            'EmergencyMobile': forms.TextInput(
                    attrs={'class': 'form-control', 
                        'placeholder': 'เบอร์มือถือ',
                        }),                                                                                                                                          
                                                                                                                
            'Comment': forms.Textarea(
                    attrs={'class': 'form-control', 
                        'rows': 3,
                        }),                                                                                                                      
        }


class PatientCOVIDForm(PatientBasicDataForm):

    def __init__(self, *args, **kwargs):
        super(PatientBasicDataForm, self).__init__(*args, **kwargs)
        self.fields['DatePositive'].widget = forms.DateInput(
                                                format=('%Y-%m-%d'),
                                                attrs={'class': 'form-control', 
                                                    'placeholder': 'Select a date',
                                                    'type': 'date'
                                                    })
        self.fields['InfectiousName'].widget = forms.Select(
                                                attrs={'class': 'form-control', 
                                                    })
        self.fields['Corona3'].widget = forms.FileInput(attrs={'class': 'form-control'})
        self.fields['DetectedResult'].widget = forms.FileInput(attrs={'class': 'form-control'})
        self.fields['ConfirmedPatient'].widget = forms.CheckboxInput(attrs={'class': 'form-control',})
        
    class Meta(PatientBasicDataForm.Meta):
        fields = PatientBasicDataForm.Meta.fields + [
                    'DatePositive',
                    'InfectiousName',
                    'Corona3',
                    'DetectedResult',
                    'ConfirmedPatient',                    
                ]
        exclude = PatientBasicDataForm.Meta.exclude + [                    
                    'ConfirmUser',
                ]

           

class PatientForm(PatientBasicDataForm):

    def __init__(self, *args, **kwargs):
        super(PatientBasicDataForm, self).__init__(*args, **kwargs)
        self.fields['EmergencyMobile'].widget.attrs['class'] = 'form-control'

    class Meta(PatientBasicDataForm.Meta):
        model = Patient
        fields = '__all__'         
        exclude = (                    
                    'DataUser',
                    'ConfirmUser',
                    'ConfirmedPatient',
                    'CurrentStatus', 
                    'CurrentTreatment',
        )      
          


class StatusLogForm(ModelForm):
    class Meta:
        model = StatusLog
        fields = ('Date', 'Status', 'Comment')
        # exclude = ('ThePatient','RecorderUser')
        widgets = {
            'Date': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
            'Status': forms.Select(
                    attrs={'class': 'form-control', 
                        }),
            'Comment': forms.Textarea(
                    attrs={'class': 'form-control', 
                        'rows': 3,
                        }), 
        }

class TreatmentLogForm(ModelForm):
    class Meta:
        model = TreatmentLog
        fields = ('Date', 'Treatment', 'Comment')
        # exclude = ('ThePatient','RecorderUser')

        widgets = {
            'Date': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }) ,
            'Treatment': forms.Select(
                    attrs={'class': 'form-control', 
                        }),
            'Comment': forms.Textarea(
                    attrs={'class': 'form-control', 
                        'rows': 3,
                        }), 
        }