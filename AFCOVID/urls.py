from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth import views as authviews
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from UserData.forms import MyLoginView
from django.shortcuts import render

@login_required
def TestPage(request):
    return render(request,"_milk.html")

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('login/', MyLoginView.as_view(), name = 'login'),
    path('logout/', authviews.LogoutView.as_view(), name = 'logout'),
   
    path('', include('Patient.urls')),
    path('tp', TestPage),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)