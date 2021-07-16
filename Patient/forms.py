from django.db import models
from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets

from Patient.models import Patient 

class PatientForms(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ('DataUser')

        widgets = {
            'Date' : forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-contral',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'BirthDay' : forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-contral',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'DatePositive' : forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-contral',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }