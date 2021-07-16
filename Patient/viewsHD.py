from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect

from Patient.forms import PatientForm
from Patient.models import Patient

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

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         obj = form.save(commit=False)
    #         obj.DataUser = request.user
    #         obj.save()
    #         messages.success(request, f'Your order has been placed.')
    #     return redirect('Patient:List')

class PatientListView(ListView):
    model = Patient
    template_name = 'Patient/List.html'
    paginate_by = 20
    ordering = ['Date',]

# class PatientUpdateView(PermissionRequiredMixin,UpdateView):
class PatientUpdateView(UpdateView):
    # permission_required = 'Patient.change_patient'

    model = Patient
    # fields = '__all__'
    form_class = PatientForm
    template_name = 'Patient/Update.html'    
    success_url = reverse_lazy('Patient:List')