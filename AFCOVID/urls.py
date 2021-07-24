from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth import views as authviews
from django.conf import settings
from UserData.forms import MyLoginView

from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from UserData.forms import MyLoginView
from django.shortcuts import render



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', MyLoginView.as_view(), name='login'),    
    # path('', home, name="home"),
    # path('admin/', admin.site.urls, name = 'admin'),
    # path('login/', MyLoginView.as_view(), name = 'login'),
    # path('logout/', authviews.LogoutView.as_view(), name = 'logout'),
   
    path('CRN3/', include('Corona3.urls')),
    path('', include('Patient.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)