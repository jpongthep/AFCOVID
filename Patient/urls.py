from django.urls import path, include
from django.shortcuts import render

from Patient.viewsHD import (PatientAddNewView,
                             PatientListView,
                             PatientUpdateView,
                             UpdatePatientData,
                             PatientDetail,
                             DeletePatientData,
                             DeletePatientTreatmentLog,
                             DeletePatientStatusLog,
                             )

def dashboard(request):
    return render(request, "_base.html")

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
    
    # path('', views.AllListView.as_view(), name = 'List'),    
    # 
    # path('<str:pk>/delete/', views.PatientDeleteView.as_view(), name = 'delete'),

]

