from django.db import models
from django import forms
from django.forms import ModelForm

from Patient.models import (
                            Patient, 
                            StatusLog, 
                            TreatmentLog,
                            AMEDPatient,
                            RIGHT_MEDICAL_TREATMENT_CHOICE)

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
                    'AirforceType',
                    'Mobile', 
                    'Address', 
                    'EmergencyMobile', 
                    'Comment',

                    'IsAMED',
                    'CurrentStatus',
                    'CurrentTreatment',
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
            'AirforceType': forms.Select(
                    attrs={'class': 'form-control', 
                        }),  
    
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
            'IsAMED': forms.CheckboxInput(attrs={'class': 'form-control',}),                          
                            
            'CurrentStatus': forms.Select(
                    attrs={'class': 'form-control', 
                        }),   
            'CurrentTreatment': forms.Select(
                    attrs={'class': 'form-control', 
                        }),                                                                                                                                                                     
        }

    def clean_PersonID(self):
        return self.cleaned_data['PersonID'] or None


class PatientCOVIDForm(PatientBasicDataForm):

    def __init__(self, *args, **kwargs):
        super(PatientBasicDataForm, self).__init__(*args, **kwargs)

        self.fields['RightMedicalTreatment'] = forms.ChoiceField(
                                                        widget  = forms.RadioSelect, 
                                                        choices = RIGHT_MEDICAL_TREATMENT_CHOICE)
        self.fields['DatePositive'].widget = forms.DateInput(
                                                format=('%Y-%m-%d'),
                                                attrs={'class': 'form-control', 
                                                    'placeholder': 'Select a date',
                                                    'type': 'date'
                                                    })
        # self.fields['InfectiousName'].widget = forms.Select(
        #                                         attrs={'class': 'form-control', 
        #                                             })
        self.fields['Corona3'].widget = forms.FileInput(attrs={'class': 'form-control'})
        self.fields['DetectedResult'].widget = forms.FileInput(attrs={'class': 'form-control'})
        # self.fields['ConfirmedByCRC'].widget = forms.CheckboxInput(attrs={'class': 'form-control',})
        
    class Meta(PatientBasicDataForm.Meta):
        fields = PatientBasicDataForm.Meta.fields + [
                    'RightMedicalTreatment',
                    'DatePositive',
                    'InfectiousName',
                    'Corona3',
                    'DetectedResult',
                    'ConfirmedByCRC',                    
                ]
        exclude = PatientBasicDataForm.Meta.exclude + [                    
                    'ConfirmUser',
                    'ConfirmedByCRC'
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
                    'ConfirmedByCRC',
                    'CurrentStatus', 
                    'CurrentTreatment',
        )      
          


class StatusLogForm(ModelForm):
    class Meta:
        model = StatusLog
        fields = ('Date', 'Status', 'Comment')
        # exclude = ('Date',)
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
        # exclude = ('Date',)

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


class AMEDPatientBasicForm(ModelForm):
    class Meta:
        model = AMEDPatient
        fields = ('PersonID','HNNumber','ANNumber','FullName','Mobile','RightMedicalTreatment','Symtom','Report','Comment')
#         fields = ('PersonID','HNNumber','ANNumber','FullName','Mobile','Symtom','Report','Comment')
# class AMEDPatientForm(AMEDPatientBasicForm):
#         # exclude = ('HNNumber',)

#     def __init__(self, *args, **kwargs):
#         super(AMEDPatientBasicForm, self).__init__(*args, **kwargs)

#         self.fields['RightMedicalTreatment'] = forms.ChoiceField(
#                                                         widget  = forms.RadioSelect, 
#                                                         choices = RIGHT_MEDICAL_TREATMENT_CHOICE)
        
                
#     class Meta(AMEDPatientBasicForm.Meta):
#         fields = AMEDPatientBasicForm.Meta.fields + [
#                     'PersonID',
#                     'RightMedicalTreatment',
#                 ]
