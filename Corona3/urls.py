from django.conf.urls import url
from django.urls import path, include
<<<<<<< HEAD
from .views import Corona3BasicFormAddNewView
# from Corona3.views import SearchSelectAutocomplete
=======
from .views import BasicFormAddNewView, minDataAddNewView

>>>>>>> origin/DevMuek
app_name = 'Corona3'

urlpatterns = [

<<<<<<< HEAD
    path('BasicData/',Corona3BasicFormAddNewView.as_view() , name = 'BasicForm'),
    # url(r'^SearchSelect-autocomplete/$', SearchSelectAutocomplete.as_view(), name= 'SearchSelect-autocomplete',),
=======
    path('BasicData/',BasicFormAddNewView.as_view() , name = 'BasicForm'),
    path('minData/',minDataAddNewView.as_view() , name = 'minForm'),

>>>>>>> origin/DevMuek
]

