from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Patient.viewsHD import (PatientAddNewView,
                             PatientListView,
                             PatientUpdateView,
                             UpdatePatientData,
                             PatientDetail,
                             DeletePatientData,
                             DeletePatientTreatmentLog,
                             DeletePatientStatusLog,
                             dashboard
                             )

from Patient.views import export_users_csv, export_Patient_csv

app_name = 'Patient'

urlpatterns = [
   
    path('AddNew', PatientAddNewView.as_view(), name = 'AddNew'),
    path('',dashboard, name = 'Dashboard'),
    path('<int:PatientType>/List',PatientListView.as_view(), name = 'List'),
    path('<int:pk>/detail', PatientDetail, name = 'Detail'),
    path('<int:pk>/update', PatientUpdateView.as_view(), name = 'Update'),
    path('<int:pk>/delete', DeletePatientData, name = 'Delete'),
    path('<int:PatientPk>/<int:treatmentPk>/DelTreatment', DeletePatientTreatmentLog, name = 'DelTreatment'),
    path('<int:PatientPk>/<int:statusPk>/DelStatus', DeletePatientStatusLog, name = 'DelStatus'),
    path('<int:pk>/updateFB', UpdatePatientData, name = 'UpdateFB'),
    
    path('export/csv/', export_users_csv, name='export_users_csv'),
    path('exportp/csv/', export_Patient_csv, name='export_Patient_csv'),
  
]

