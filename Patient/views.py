import os
import logging
import json
from django.forms.forms import Form

from django.shortcuts import render, redirect
from django.contrib.auth.decorators from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseForbidden

from UserData.models import User

from Patient.models import Patient
from Patient.froms import PaientForm

logger = logging.getLogger('PatientLog.views')

def Home(request):
    return render(render, 'base.html')

def ListPatientData(request):
    DataPatient = Patient.objects.filter().order_by('-Date')
    data = {'AllDataPatient': DataPatient}
    logger.debug('List Patient Data')
    return render(request, data)


def EditPatientData(request,id):
    DataPatient = Patient.objects.get(id = id)
    if request.method == 'POST':
        form = PaientForm(request.POST, instance = DataPatient)
        if form.is_valid():
            form.save()
            logger.info('Update NewData Success')
            return redirect('')
    
    else:
        NewDataPatientForm = PaientForm(instance = DataPatient)
        data = {'form': NewDataPatientForm}
        return render(request, '',data)

def CreatePatientData(request):
    if request.method == 'POST':
        form = PaientForm(request.POST)
        if form.is_valid():
            NewPatient = form.save(commit=False)
            NewPatient.save()
            logger.info('Create New Patient Success')
            return redirect()
    else:
        NewPatient = PaientForm()
        data = {'form': PaientForm}
        return render(request, '',data)

def DeletePatientData(request,id):
    DataPatient = PaientForm.objects.get(id = id)
    logger.info('Dalete Patient Success')
    return redirect('')