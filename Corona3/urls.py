from django.conf.urls import url
from django.urls import path, include
from .views import BasicFormAddNewView, minDataAddNewView

app_name = 'Corona3'

urlpatterns = [

    path('BasicData/',BasicFormAddNewView.as_view() , name = 'BasicForm'),
    path('minData/',minDataAddNewView.as_view() , name = 'minForm'),

]

