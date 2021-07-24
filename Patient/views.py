import csv
import codecs

from django.http import HttpResponse
from UserData.models import User

from Patient.viewsHD import PatientListView

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    response.write(codecs.BOM_UTF8)

    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response

def export_Patient_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    response.write(codecs.BOM_UTF8)

    writer = csv.writer(response)
    Queryset = PatientListView.get_queryset(request)

    writer.writerow(['Username', 'First name', 'Last name','Username', 'First name', 'Last name', 'Email address'])

    users = Queryset.objects.all()
    for user in users:
        writer.writerow(user)

    return response