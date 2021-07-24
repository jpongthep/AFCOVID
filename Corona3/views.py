import os
import logging
import json
from django.forms.forms import Form

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseForbidden

# from UserData.models import User

from Corona3.models import Corona3
from Corona3.forms import Corona3BasicDataForm

logger = logging.getLogger('Corona3Log.views')

def Home(request):
    return render(render, 'base.html')

def ListCorona3Data(request):
    DataCorona3 = Corona3.objects.filter().order_by('-Date')
    data = {'AllDataPatient': DataCorona3}
    logger.debug('List Corona3 Data')
    return render(request, data)


def EditCorona3Data(request,id):
    DataCorona3 = Corona3.objects.get(id = id)
    if request.method == 'POST':
        form = Corona3BasicDataForm(request.POST, instance = DataCorona3)
        if form.is_valid():
            form.save()
            logger.info('Update NewData Success')
            return redirect('')
    
    else:
        NewDataCorona3Form = Corona3BasicDataForm(instance = DataCorona3)
        data = {'form': NewDataCorona3Form}
        return render(request, '',data)

def CreateCorona3Data(request):
    if request.method == 'POST':
        form = Corona3BasicDataForm(request.POST)
        if form.is_valid():
            NewCorona3 = form.save(commit=False)
            NewCorona3.save()
            logger.info('Create New Corona3 Success')
            return redirect()
    else:
        NewCorona3 = Corona3BasicDataForm()
        data = {'form': Corona3BasicDataForm}
        return render(request, '',data)

def DeleteCorona3Data(request,id):
    DataCorona3 = Corona3BasicDataForm.objects.get(id = id)
    logger.info('Dalete Corona3 Success')
    return redirect('')