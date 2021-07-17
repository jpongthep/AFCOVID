from django.db import models
from django import forms
from django.forms import ModelForm

from Patient.models import Patient

class PatientBaseForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ('DataUser','ConfirmUser')

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
            'InfectiousName': forms.Select(
                    attrs={'class': 'form-control', 
                        'placeholder': 'ผู้ติดเชื้อที่ใกล้ชิด',
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
            'IsAirforce': forms.CheckboxInput(
                    attrs={'class': 'form-control', 
                        }),                          
            'DatePositive': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
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
            'Comment': forms.Textarea(
                    attrs={'class': 'form-control', 
                        'rows': 3,
                        }),                                                                                                                      
        }


class PatientForm(PatientBaseForm):

    def __init__(self, *args, **kwargs):
        super(PatientBaseForm, self).__init__(*args, **kwargs)
        self.fields['EmergencyMobile'].widget.attrs['class'] = 'form-control'

    class Meta(PatientBaseForm.Meta):
        model = Patient
        fields = '__all__'
        exclude = ('DataUser','ConfirmUser','ConfirmedPatient', )
