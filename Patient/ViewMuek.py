import os
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from django.db.models import Q

from django.shortcuts import get_object_or_404, redirect

from Patient.models import AMEDPatient, Patient
from django.shortcuts import render, redirect
from Patient.forms import StatusLog, AMEDPatientBasicForm

class AMEDPatientListView(LoginRequiredMixin,ListView):
    login_url = '/login'
    model = AMEDPatient
    # fields = '__all__'
    template_name = 'AMED/AmedList.html'
    paginate_by = 10
    ordering = ['-id']
    def form_invalid(self, form):
        print(self.request, form.errors)
        return super().form_invalid(form)
    
    def get_queryset(self) :
        queryset = AMEDPatient.objects.all()   
        nameSearch = self.request.GET.get('textsearch')
        HNNumberSearch = self.request.GET.get('HNNumber')
        ANNumberSearch = self.request.GET.get('ANNumber')
        # print('nameSearch = ',nameSearch)

        if nameSearch:
            queryset = queryset.filter(Q(FullName__icontains = nameSearch) | Q(PersonID = nameSearch))

        if HNNumberSearch:
            queryset = queryset.filter(HNNumber = HNNumberSearch)

        if ANNumberSearch:
            queryset = queryset.filter(ANNumber = ANNumberSearch)
        
        return queryset.order_by('-PersonID','-FullName')

            

def AmedPatientDetail(request, pk):
    aAmedPatient = get_object_or_404(AMEDPatient, id = pk)
   
    context = {
        "AMEDPatient" :  aAmedPatient, 
            }

    return render(request, "AMED/AmedPatientDetail.html", context)