from django.conf.urls import url
from django.urls import path, include
from .views import (BasicFormAddNewView, 
                    minDataAddNewView, 
                    Corona3ListView,
                    Corona3UpdateView,
                    corona3_Document)

from .views_selenium import automate_addpatient

app_name = 'Corona3'

urlpatterns = [
    path('BasicData/',BasicFormAddNewView.as_view() , name = 'BasicForm'),
    path('minData/',minDataAddNewView.as_view() , name = 'minForm'),
    path('list/',Corona3ListView.as_view() , name = 'list'),
    path('<pk>/up/',Corona3UpdateView.as_view() , name = 'update'),
    path('<pk>/doc/',corona3_Document , name = 'doc'),
    path('<pk>/export/',automate_addpatient , name = 'export'),
]

