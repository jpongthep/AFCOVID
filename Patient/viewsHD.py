from datetime import timedelta

from django.utils import timezone
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count, F

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.forms import formset_factory
from django.db.models import Q
from django.contrib.auth.models import Group

from Patient.forms import ( PatientCOVIDForm,
                            PatientForm, 
                            StatusLogForm, 
                            TreatmentLogForm)

from Patient.models import (Patient,
                            StatusLog,
                            TreatmentLog)

@login_required
def dashboard(request,num_day = 7):
    last7day = timezone.now().date() - timedelta(days=num_day)
    yesterday = timezone.now().date() - timedelta(days=1)
    today = timezone.now().date()
    PatientCount = Patient.objects.filter(Date__range=(last7day,today)
                                 ).order_by('Date'
                                 ).values(
                                     'Date',
                                     week_day = F('Date__week_day')
                                 ).annotate(NumPatient = Count('id'))
    
    UnitCount = Patient.objects.filter(Date__range=(last7day,today)
                                 ).filter(AirforceType = 1
                                 ).order_by('Office'
                                 ).values('Office'
                                 ).annotate(NumPatient = Count('id'))

    
    context = {
            'PatientCount' : PatientCount, 
            'UnitCount' : UnitCount,
            'NumDay' : num_day,
            'ChartWidth' : 500 + (num_day - 7)* 50 if num_day > 7 else 500}
    # print('PatientCount : ',PatientCount)


    return render(request, "Patient/dashboard.html",context)


def get_form_class(user):
    IsAFCMO = user.has_perm('UserData.User_AF_CMO')
    IsUnitCMO = user.has_perm('UserData.User_Unit_CMO')
    IsCRC = user.has_perm('UserData.User_CRC')

    if IsCRC:
        print("User CRC Form")
        return PatientCOVIDForm
    elif IsAFCMO or IsUnitCMO:
        return PatientCOVIDForm
        # print("User Basic Form")
        # return PatientBasicDataForm    
    else:
        return PatientCOVIDForm
        # return PatientForm

def get_template_name(user):
    IsAFCMO = user.has_perm('UserData.User_AF_CMO')
    IsUnitCMO = user.has_perm('UserData.User_Unit_CMO')

    if IsAFCMO or IsUnitCMO:
        return 'Patient/List.html'
    else:
        return 'Patient/List.html' #'Patient/ListAFCMO.html'

class PatientAddNewView(CreateView):
    login_url = '/login'
    model = Patient
    # fields = '__all__'
    form_class = PatientForm
    template_name = 'Patient/AddNew.html'   
    success_url = '/0/List' 
    
    def get_form_class(self):
        return get_form_class(self.request.user)

    def form_valid(self, form):
        print('Create Check Form - Valid start')
        if self.request.user.has_perm("UserData.User_CRC"):
            a = form.save(commit=False)
            a.DataUser = self.request.user
            a.ConfirmUser = self.request.user
            a.ConfirmedByCRC = True
            a.save()
        else:
            form.save()

        print('Create Check Form - Valid end')
        messages.info(self.request,f'บันทึกข้อมูล {a.FullName} เรียบร้อย')

        return redirect(reverse('Patient:List', kwargs={'PatientType': 0}))

 
class PatientListView(LoginRequiredMixin,ListView):
    login_url = '/login'
    model = Patient
    template_name = 'Patient/List.html'
    paginate_by = 10
    ordering = ['-Date','-id']

    def get_template_names(self):
        return get_template_name(self.request.user)

    def get_context_data(self, **kwargs):
        context = super(PatientListView, self).get_context_data(**kwargs)

        PatientType = self.kwargs['PatientType']
        self.request.session['PatientType'] = PatientType

        print('PatientType',PatientType)
        if PatientType == 0:
            context['PageTitle'] = "ผู้ป่วยทั้งหมด"
        elif PatientType == 1:
            context['PageTitle'] = "ผู้ป่วย AMED"
        elif PatientType == 4:
            context['PageTitle'] = "ผู้ป่วย ทอ."
        elif PatientType == 2:
            context['PageTitle'] = "ผู้ป่วยพลทหาร"
        elif PatientType == 3:
            context['PageTitle'] = "ผู้ป่วยนอกจากพลทหาร"
    
        return context

    def get_queryset(self) :
        PatientType = self.kwargs['PatientType']
        self.request.session['PatientType'] = PatientType

        print('PatientType',PatientType)
        if PatientType == 0:
            queryset = Patient.objects.all()   
        elif PatientType == 4:
            queryset = Patient.objects.filter(IsAMED = True)
        else:
            queryset = Patient.objects.filter(AirforceType = PatientType)            

        nameSearch = self.request.GET.get('textsearch')
        dateSearch = self.request.GET.get('date')
        OfficeSearch = self.request.GET.get('Office')
        # print('nameSearch = ',nameSearch)

        if nameSearch:
            queryset = queryset.filter(Q(FullName__icontains = nameSearch) | Q(PersonID = nameSearch))

        if dateSearch:
            queryset = queryset.filter(Date = dateSearch)

        if OfficeSearch:
            queryset = queryset.filter(Office = OfficeSearch)
        
        return queryset.order_by('-Date','-FullName')
       

def SaveStatusTreatment(request, pk):
    aPatient = get_object_or_404(Patient, id = pk)

    status_log_form = StatusLogForm(request.POST, prefix='status')
    treatment_log_form = TreatmentLogForm(request.POST, prefix='treatment')
    print(request.POST)
    print(status_log_form)
    if status_log_form.is_valid() and request.POST['status-Date']:
        form = status_log_form.save(commit = False)
        form.RecorderUser = request.user
        form.ThePatient = aPatient
        form.save()
        messages.info(request,f'บันทึกสถานะของ "{aPatient}" เรียบร้อย')
    if treatment_log_form.is_valid() and request.POST['treatment-Date']:
        form = treatment_log_form.save(commit=False)
        form.RecorderUser = request.user
        form.ThePatient = aPatient
        form.save()
        messages.info(request,f'บันทึกการรักษาของ "{aPatient}" เรียบร้อย')

@login_required
def PatientDetail(request, pk):
    aPatient = get_object_or_404(Patient, id = pk)
    if request.method == 'POST':
        SaveStatusTreatment(request, pk)        

    status_log_form = StatusLogForm(prefix='status')
    treatment_log_form = TreatmentLogForm(prefix='treatment')

    StatusList = StatusLog.objects.filter(ThePatient = aPatient).order_by('-Date')
    TreatmentList = TreatmentLog.objects.filter(ThePatient = aPatient).order_by('-Date')        
    context = {
                "Patient" :  aPatient, 
                'StatusList' : StatusList,
                'TreatmentList' : TreatmentList,
                'status_log_form' : status_log_form,
                'treatment_log_form' : treatment_log_form
                }

    return render(request, "Patient/Detail.html", context)


class PatientUpdateView(LoginRequiredMixin,UpdateView):

    model = Patient
    # fields = '__all__'
    form_class = PatientForm
    template_name = 'Patient/Update.html'  

    def get_success_url(self):
        PatientType = self.request.session.get('PatientType',0)
        print('PatientType',PatientType)
        messages.info(request,f'บันทึกการ update ข้อมูล เรียบร้อย')
        return reverse('Patient:List', kwargs={'PatientType': PatientType})


@login_required
def DeletePatientData(request,pk):
    patient = Patient.objects.get(id = pk)
    if patient.DataUser == request.user:
        patient.delete()
        messages.info(request,f'ลบข้อมูลของ {patient.FullName} เรียบร้อย')
        return redirect(reverse('Patient:List', kwargs={'PatientType': 0}))  
    else:
        return HttpResponse(f'<h1>ไม่สามารถลบข้อมูลผู้ป่วยที่ผู้อื่นกรอกได้</h1> <p>ผู้ขอลบ : {request.user.FullName}</p> <p>ผู้กรอกข้อมูล : {patient.DataUser.FullName}</p>')

@login_required
def DeletePatientTreatmentLog(request,PatientPk, treatmentPk):
    treatment = TreatmentLog.objects.get(id = treatmentPk)
    treatment.delete()
    return redirect('Patient:Detail', pk=PatientPk) 
            
@login_required
def DeletePatientStatusLog(request,PatientPk, statusPk):
    status = StatusLog.objects.get(id = statusPk)
    status.delete()
    return redirect('Patient:Detail', pk=PatientPk) 
    

@login_required
def UpdatePatientData(request, pk):
    context ={}

    obj = get_object_or_404(Patient, id = pk)

    UserForm = get_form_class(request.user)
    form = UserForm(request.POST or None, request.FILES or None, instance = obj)
 
    if form.is_valid():
        patientFullName = request.POST["FullName"]
        if request.user.has_perm("UserData.User_CRC"):
            a = form.save(commit=False)
            a.ConfirmUser = request.user
            a.ConfirmedByCRC = True
            a.save()
        else:
            form.save()

        messages.info(request,f"Update ข้อมูล '{patientFullName}' เรียบร้อย")
        return redirect(reverse_lazy('Patient:List', kwargs={'PatientType': 0}))
 
    context["form"] = form
 
    return render(request, "Patient/Update.html", context)