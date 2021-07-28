
from django.forms.forms import Form
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect

from .models import Corona3
from .forms import BasicDataForm


class BasicFormAddNewView(CreateView):

    model = Corona3
    form_class = BasicDataForm
    template_name = 'Corona3/basicData.html' 
    success_url = '/CRN3/BasicData/'
    
    def form_invalid(self, form):
        print(self.request, form.errors)
        return super().form_invalid(form)
    
    def post(self, request):
        super(BasicFormAddNewView, self).post(request)
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        return redirect('/CRN3/BasicData/')

class minDataAddNewView(CreateView):

    model = Corona3
    form_class = BasicDataForm
    template_name = 'Corona3/minData.html' 
    success_url = '/CRN3/BasicData/'
    
    def form_invalid(self, form):
        print(self.request, form.errors)
        return super().form_invalid(form)
    
    def post(self, request):
        super(BasicFormAddNewView, self).post(request)
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        return redirect('/CRN3/BasicData/')




    
