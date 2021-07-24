from django.urls import path, include
from .views import Corona3BasicForm

app_name = 'Corona3'

urlpatterns = [

    path('BasicData/',Corona3BasicForm , name = 'BasicForm'),

]

