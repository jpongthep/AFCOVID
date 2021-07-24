
from django.forms.forms import Form
from django.views.generic import CreateView

from .models import Corona3
from .forms import Corona3BasicDataForm


class Corona3BasicFormAddNewView(CreateView):

    model = Corona3
    form_class = Corona3BasicDataForm
    template_name = 'Corona3/basicData.html' 
    success_url = '/CRN3/BasicData/'   
    
