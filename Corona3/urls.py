from django.urls import path, include
from .views import Corona3BasicFormAddNewView

app_name = 'Corona3'

urlpatterns = [

    path('BasicData/',Corona3BasicFormAddNewView.as_view() , name = 'BasicForm'),

]

