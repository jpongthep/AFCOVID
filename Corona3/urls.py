from django.urls import path, include

from Corona3.views import ListCorona3Data, EditCorona3Data, CreateCorona3Data
# (Corona3AddNewView, Corona3ListView, Corona3UpdateView, Corona3PatientData, Corona3Detail,)
                                                        #  Corona3PatientData



app_name = "Corona3"

urlpatterns = [
   
    # path('AddNew', Corona3AddNewView.as_view(), name = 'AddNew'),
    path('AddNew', CreateCorona3Data.as_view(), name = 'AddNew'),
    # path('',Corona3ListView.as_view(), name = 'List'),
    path('',ListCorona3Data.as_view(), name = 'List'),
    # path('<int:pk>/detail', Corona3Detail, name = 'Detail'),
    path('<int:pk>/detail', Corona3Detail, name = 'Detail'),
    # path('<int:pk>/update', Corona3UpdateView.as_view(), name = 'Update'),
    path('<int:pk>/update', EditCorona3Data.as_view(), name = 'Update'),
    # path('<int:pk>/delete', DeleteCorona3Data, name = 'Delete'),
    # path('<int:pk>/updateFB', UpdateCorona3Data, name = 'UpdateFB'),
    # path('Infect', InfectListView.as_view(), name = 'Infect'),
    
    # path('', views.AllListView.as_view(), name = 'List'),    
    # 
    # path('<str:pk>/delete/', views.PatientDeleteView.as_view(), name = 'delete'),

]

