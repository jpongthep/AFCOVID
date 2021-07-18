from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth import views as authviews
from django.conf import settings
from django.conf.urls.static import static
from UserData.forms import MyLoginView

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('login/', MyLoginView.as_view(), name = 'login'),
    path('logout/', authviews.LogoutView.as_view(), name = 'logout'),
   
    path('', include('Patient.urls')),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
