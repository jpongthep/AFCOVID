<<<<<<< HEAD
import csv
import codecs

from django.http import HttpResponse
from UserData.models import User

from Patient.viewsHD import PatientListView

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    response.write(codecs.BOM_UTF8)

    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response

def export_Patient_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    response.write(codecs.BOM_UTF8)

    writer = csv.writer(response)
    Queryset = PatientListView.get_queryset(request)

    writer.writerow(['Username', 'First name', 'Last name','Username', 'First name', 'Last name', 'Email address'])

    users = Queryset.objects.all()
    for user in users:
        writer.writerow(user)

    return response
=======
import os
import logging
import json
from django.forms.forms import Form

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
>>>>>>> AfcovidMuek
