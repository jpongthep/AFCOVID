
from django.forms.forms import Form
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect

from .models import Corona3
from .forms import Corona3BasicDataForm


class Corona3BasicFormAddNewView(CreateView):

    model = Corona3
    form_class = Corona3BasicDataForm
    template_name = 'Corona3/basicData.html' 
    success_url = '/CRN3/BasicData/'
    
    def form_invalid(self, form):
        print(self.request, form.errors)
        return super().form_invalid(form)
    
    def post(self, request):
        super(Corona3BasicFormAddNewView, self).post(request)
        messages.success(request, 'ส่งข้อมูลเรียบร้อยแล้ว')
        return redirect('/CRN3/BasicData/')




    
