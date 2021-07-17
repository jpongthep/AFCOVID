from django.urls import path, include

from Patient.viewsHD import (PatientAddNewView,
                             PatientListView,
                             PatientUpdateView,
                             UpdatePatientData,
                             PatientDetail
                             )


app_name = "Patient"

urlpatterns = [
   
    path('AddNew', PatientAddNewView.as_view(), name = 'AddNew'),
    path('',PatientListView.as_view(), name = 'List'),
    path('<int:pk>/detail', PatientDetail, name = 'Detail'),
    path('<int:pk>/update', PatientUpdateView.as_view(), name = 'Update'),
    path('<int:pk>/updateFB', UpdatePatientData, name = 'UpdateFB'),
    
    # path('', views.AllListView.as_view(), name = 'List'),    
    # 
    # path('<str:pk>/delete/', views.PatientDeleteView.as_view(), name = 'delete'),

]

