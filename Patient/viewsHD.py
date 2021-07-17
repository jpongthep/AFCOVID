from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.forms import formset_factory
from django.db.models import Q


from Patient.forms import PatientForm, StatusLogForm, TreatmentLogForm
from Patient.models import (Patient,
                            StatusLog,
                            TreatmentLog)

# class AddNewView(LoginRequiredMixin,CreateView):
class PatientAddNewView(CreateView):
    # login_url = '/admin/'
    model = Patient
    # fields = '__all__'
    form_class = PatientForm
    template_name = 'Patient/AddNew.html'    
    success_url = reverse_lazy('Patient:List')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.DataUser = self.request.user
        self.object.save()
        messages.info(self.request,"Save Success")
        return HttpResponseRedirect(self.get_success_url())

class InfectListView(LoginRequiredMixin,ListView):
    login_url = '/login'
    template_name = 'Patient/List.html'
    paginate_by = 5
    ordering = ['Date',]

    def get_queryset(self) :
        queryset = Patient.objects.filter(IsAirforce = True)
        return queryset

    def get_template_names(self):
        # print(self.request.user)
        # print(self.request.user.has_perm('UserData.User_AF_CMO'))
        if self.request.user.has_perm('UserData.User_AF_CMO'):
            return 'Patient/List.html'
        else:
            return 'Patient/ListAFCMO.html'

class PatientListView(LoginRequiredMixin,ListView):
    login_url = '/login'
    model = Patient
    template_name = 'Patient/List.html'
    paginate_by = 5
    ordering = ['Date',]

    def get_template_names(self):
        # print(self.request.user)
        # print(self.request.user.has_perm('UserData.User_AF_CMO'))
        if self.request.user.has_perm('UserData.User_AF_CMO'):
            return 'Patient/List.html'
        else:
            return 'Patient/ListAFCMO.html'

def SaveStatusTreatment(request, pk):
    aPatient = get_object_or_404(Patient, id = pk)

    DateList = request.POST.getlist('Date')        
    status_log_form = StatusLogForm(request.POST)
    treatment_log_form = TreatmentLogForm(request.POST)
    print(request.POST)
    print(status_log_form)
    if status_log_form.is_valid() and DateList[0]:
        form = status_log_form.save(commit = False)
        form.Date = DateList[0]
        form.RecorderUser = request.user
        form.ThePatient = aPatient
        form.save()
        messages.info(request,'Save Status success')
    if treatment_log_form.is_valid() and DateList[1]:
        form = treatment_log_form.save(commit=False)
        form.RecorderUser = request.user
        form.ThePatient = aPatient
        form.save()
        messages.info(request,'Save Treatment success')

def PatientDetail(request, pk):
    aPatient = get_object_or_404(Patient, id = pk)
    if request.method == 'POST':
        SaveStatusTreatment(request, pk)        

    status_log_form = StatusLogForm()
    treatment_log_form = TreatmentLogForm()

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



# class PatientUpdateView(PermissionRequiredMixin,UpdateView):
class PatientUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = 'Patient.change_patient'

    model = Patient
    # fields = '__all__'
    form_class = PatientForm
    template_name = 'Patient/Update.html'    
    success_url = reverse_lazy('Patient:List')


def UpdatePatientData(request, pk):
    context ={}

    obj = get_object_or_404(Patient, id = pk)
 
    form = PatientForm(request.POST or None, request.FILES or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return redirect(reverse_lazy('Patient:List'))
 
    context["form"] = form
 
    return render(request, "Patient/Update.html", context)