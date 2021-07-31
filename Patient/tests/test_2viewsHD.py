from django import urls
from django.contrib.auth import get_user_model
import pytest

from UserData.models import User
from Patient.models import Patient


def login_user():
    username = "user1"
    password = "bar"
    logined_user = User.objects.create_user(username=username, password=password)
    # perm = Permission.objects.get(codename='can_approve_requests')
    # user.user_permissions.add(perm)
    return logined_user

@pytest.mark.parametrize('param',[
    ('login'),
    ('Corona3:BasicForm'),
    ('Corona3:minForm'),
])
def test_render_views(client,param):
  

    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200

@pytest.mark.django_db
def test_add_patient(client, patient_data):
    LoginUser = login_user();
    client.force_login(LoginUser)
    patient = Patient
    assert patient.objects.count() == 0
    AddNewPatientURL = urls.reverse('Patient:AddNew')
    resp = client.post(AddNewPatientURL, patient_data)
    
    # assert patient.objects.get(PersonID = "1234567890123").FullName == "NewPatient"
    assert patient.objects.count() == 1 

@pytest.mark.django_db
def test_user_login(client,create_test_user,user_data):
    assert User.objects.count() == 1
    login_url = urls.reverse('login')
    resp = client.post(login_url, data = user_data)
    assert resp.status_code == 200
    # assert resp.url == urls.reverse('Patient:Dashboard7')