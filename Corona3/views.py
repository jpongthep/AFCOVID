import os
from io import StringIO, BytesIO

#django module
from django.forms.forms import Form
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings

#3rd party module
from docx import Document

from .models import Corona3
from .forms import BasicDataForm, minDataForm


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
    form_class = minDataForm
    template_name = 'Corona3/minData.html' 
    success_url = '/CRN3/minData/'
    
    def form_invalid(self, form):
        print(self.request, form.errors)
        return super().form_invalid(form)
    
    def post(self, request):
        super(minDataAddNewView, self).post(request)
        messages.success(request,"บันทึกข้อมูลเรียบร้อยแล้ว")
        return redirect('/CRN3/minData/')

class Corona3ListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Corona3
    template_name = 'Corona3/list.html'
    ordering = ['-DateReport','-id']    
    paginate_by = 10

class Corona3UpdateView(LoginRequiredMixin,UpdateView):
    model = Corona3
    form_class = BasicDataForm
    template_name = 'Corona3/basicData.html'
    success_url = '/CRN3/list/'


def corona3_Document(request,pk):
    # testdoc = static('documents/form_corona3.docx')
    testdoc =  os.path.join(settings.TEMPLATES[0]['DIRS'][0],'documents/form_corona3.docx')

    document = Document(testdoc)

    corona3 = Corona3.objects.get(id = pk)
    docx_title= f"Corona3-{pk}.docx"

    time_and_date = "2019-10-21"
    employee_name = corona3.FullName
    manager_name = "Michelle Johnson"

    dic = {
            '#Fullname#':corona3.FullName,
            '#PersonID#':corona3.PersonID,            
            '#Gender#':corona3.get_Gender_display(),            
            }
    print(dic)

    for para in document.paragraphs:
        for key, value in dic.items():
            if key in para.text:
                inline = para.runs
                # Loop added to work with runs (strings with same style)
                for i in range(len(inline)):
                    if key in inline[i].text:
                        text = inline[i].text.replace(key, value)
                        inline[i].text = text

    # Prepare document for download        
    # -----------------------------
    f = BytesIO()
    document.save(f)
    length = f.tell()
    f.seek(0)
    response = HttpResponse(
        f.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    print('docx_title = ',docx_title)
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(docx_title)
    response['Content-Length'] = length
    return response








    


    