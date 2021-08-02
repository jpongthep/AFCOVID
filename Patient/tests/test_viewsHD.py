import pytest
import json 

from datetime import date
# from django.contrib.auth.models import AnonymousUser, User
from UserData.models import User
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer


from Patient import viewsHD
from Patient.models import Patient
from UserData.models import User
# from myapp.forms import MyModelForm
# from myapp.models import MyModel

pytestmark = pytest.mark.django_db



def login_user():
    username = "test_user"
    password = "bar"
    logined_user = User.objects.create_user(username=username, password=password)
    # perm = Permission.objects.get(codename='can_approve_requests')
    # user.user_permissions.add(perm)
    return logined_user

def patient_add(DataUser,AirforceType):
    patient = Patient(
                FullName = f"TestUser {AirforceType}",
                DataUser = DataUser, 
                Date = date.today(),
                AirforceType = AirforceType
            )
    patient.save()



@pytest.mark.parametrize("AirforceType",[0,1,2,3,5,6,7])
@pytest.mark.django_db
def test_ListPage(client,AirforceType):

    LoginUser = login_user();
    client.force_login(LoginUser)

    patient_add(LoginUser,AirforceType)

    response = client.get(reverse("Patient:List", kwargs={'PatientType':AirforceType}))

    assert "TestUser " + str(AirforceType) in str(response.content)

    

# @pytest.mark.django_db
# def test_input_patient(client):

#     LoginUser = login_user();
#     client.force_login(LoginUser)

#     data = {
#         "FullName" : "NewPatient",
#         "PersonID" : "1234567890123",
#         "DataUser" : LoginUser, 
#         "Date" : date.today(),
#         "AirforceType" : 1 
#     }    
#     response = client.post(
#                     reverse("Patient:AddNew"),
#                     data=json.dumps(data),
#                     headers={"Content-Type": "application/json"},
#             )
#     self.assertEqual(201, response.status_code)
#     self.assertEqual('Your message has been successfully saved', response.data)    
    
    # req = client.post(reverse("Patient:AddNew"), data = data)


    # newPatient = Patient.objects.get(FullName = "NewPatient")
    # assert newPatient.PersonID == "1234567890123"


# def test_post(client):
#     assert False is Patient.objects.all().exists()
#     LoginUser = login_user();
#     client.force_login(LoginUser)
      
#     data = {
#         "FullName" : "NewPatient",
#         "PersonID" : "1234567890123",
#         "DataUser" : LoginUser, 
#         "Date" : date.today(),
#         "AirforceType" : 1 
#     } 
#     req = RequestFactory().post(reverse("Patient:AddNew"), data=data)
#     req.user = LoginUser
#     resp = viewsHD.PatientAddNewView.as_view()(req)
#     # assert resp.status_code == 302, "Should redirect to success url"
#     # assert resp.url == reverse('Patient:List', kwargs={'AirforceType': 0})
#     assert Patient.objects.all().exists()
#     assert Patient.objects.all()[0].FullName == "NewPatient"
#     # response = client.get(reverse("Patient:List", kwargs={'AirforceType':1}))
#     # assert "NewPatient" in str(response.content)



# class TestMyCreateView:
#     def test_authentication(self):
#         req = RequestFactory().get(reverse("myapp:mycreateview"))
#         # req.user = AnonymousUser()
#         resp = views.MyCreateView.as_view()(req)
#         assert resp.status_code == 200, "Everyone can create a MyModel"

#     def test_post(self):
#         assert False is MyModel.objects.all().exists()
#         data = {
#             "name": "Hans",
#             "other_model": mixer.blend("myapp.MyOtherModel").pk
#         }
#         req = RequestFactory().post(reverse("myapp:mycreateview"), data=data)
#         resp = views.MyCreateView.as_view()(req)
#         assert resp.status_code == 302, "Should redirect to success url"
#         assert resp.url == "/create_success/"
#         assert MyModel.objects.all().exists()
#         assert MyModel.objects.all()[0].name == "Hans"


# class TestMyUpdateView:
#     def test_authentication(self):
#         my_model = mixer.blend("myapp.MyModel")

#         req = RequestFactory().get(reverse("myapp:myupdateview", kwargs={'pk': my_model.pk}))
#         req.user = AnonymousUser()
#         resp = views.MyUpdateView.as_view()(req, pk=my_model.pk)
#         assert resp.status_code == 302, "You have to be logged in"
#         assert "login" in resp.url

#         req.user = mixer.blend(User)
#         resp = views.MyUpdateView.as_view()(req, pk=my_model.pk)
#         assert resp.status_code == 200, "Authenticaiton successfull"

#     def test_post(self):
#         my_model = mixer.blend("myapp.MyModel", name="Dieter")
#         data = {
#             "name": "Hans",
#             "other_model": my_model.other_model.pk
#         }
#         req = RequestFactory().post(reverse("myapp:myupdateview", kwargs={'pk': my_model.pk}), data=data)
#         req.user = mixer.blend(User)

#         resp = views.MyUpdateView.as_view()(req, pk=my_model.pk)
#         assert resp.status_code == 302, "redirect to success url"
#         assert "/update_success/" in resp.url
#         assert my_model.name == "Dieter"
#         my_model.refresh_from_db()
#         assert my_model.name == "Hans"
#         assert len(MyModel.objects.all()) == 1, "Should be no new objects"

#     def test_invalid_data(self):
#         my_model = mixer.blend("myapp.MyModel", name="Dieter")
#         data = {
#             "name": "Hans"
#         }
#         req = RequestFactory().post(reverse("myapp:myupdateview", kwargs={'pk': my_model.pk}), data=data)
#         req.user = mixer.blend(User)

#         resp = views.MyUpdateView.as_view()(req, pk=my_model.pk)
#         assert resp.status_code == 200, "should not redirect to success url, when data is invalid"
#         assert my_model.name == "Dieter"
#         my_model.refresh_from_db()
#         assert my_model.name == "Dieter", "Name should not have changed"
#         assert len(MyModel.objects.all()) == 1, "Should be no new objects"

#     def test_valid_form_data(self):
#         my_model = mixer.blend("myapp.MyModel", name="Dieter")
#         data = {
#             "name": "Hans",
#             "other_model": mixer.blend("myapp.MyOtherModel").pk
#         }

#         form = MyModelForm(data=data)
#         assert form.is_valid()
#         req = RequestFactory().post(reverse("myapp:myupdateview", kwargs={'pk': my_model.pk}), data=form.data)
#         req.user = mixer.blend(User)

#         resp = views.MyUpdateView.as_view()(req, pk=my_model.pk)
#         assert resp.status_code == 302, "should redirect to success url"
#         assert my_model.name == "Dieter"
#         my_model.refresh_from_db()
#         assert my_model.name == "Hans", "Name should have changed"
#         assert len(MyModel.objects.all()) == 1, "Should be no new objects"