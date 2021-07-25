from django.conf.urls import url
from django.urls import path, include
from .views import Corona3BasicFormAddNewView
# from Corona3.views import SearchSelectAutocomplete
app_name = 'Corona3'

urlpatterns = [

    path('BasicData/',Corona3BasicFormAddNewView.as_view() , name = 'BasicForm'),
    # url(r'^SearchSelect-autocomplete/$', SearchSelectAutocomplete.as_view(), name= 'SearchSelect-autocomplete',),
]

