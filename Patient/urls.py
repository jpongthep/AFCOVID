from django.urls import path, include

from Patient.viewsHD import (PatientAddNewView,
                             PatientListView,
                             PatientUpdateView)


app_name = 'Patient'

urlpatterns = [
   
    path('AddNew', PatientAddNewView.as_view(), name = 'AddNew'),
    path('List',PatientListView.as_view(), name = 'List'),
    path('<int:pk>/update', PatientUpdateView.as_view(), name = 'Update'),
    
    # path('', views.AllListView.as_view(), name = 'List'),    
    # 
    # path('<str:pk>/delete/', views.PatientDeleteView.as_view(), name = 'delete'),

]

