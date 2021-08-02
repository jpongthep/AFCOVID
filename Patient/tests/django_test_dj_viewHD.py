from datetime import date

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls.base import reverse

from Patient.models import Patient
from UserData.models import User

# User = get_user_model()


class UserModelTest(TestCase):

    username = 'test_user'
    password = 'asdfasdfasdf'


    def setUp(self):
        # Every test needs access to the request factory.
        self.user = User.objects.create_user(username=self.username, password=self.password)
    
    # def test_user_is_valid(self):
        
    #     title = 'new Title From test'
        
    #     self.client.login(username=self.username, password=self.password)
    #     response = self.client.post('http://127.0.0.1:8000/create', {
    #         'user':self.client,
    #         'title':title
    #     })
    #     post = Post.objects.all().first()
    #     self.assertEqual(post.title, title)
    #     self.assertEqual(post.user, self.user)

    #     self.assertEqual(response.status_code, 302)
    
    # def test_user_is_NOT_valid(self):
    #     response = self.client.get('http://127.0.0.1:8000/create')
    #     self.assertEqual(response.status_code, 302)

    def test_dashboard7(self):
        self.client.login(username=self.username, password=self.password)

        
        # using the client, self.client, make the POST request
        response = self.client.get(reverse('Patient:Dashboard7'))

        self.assertEqual(response.status_code,200)
      

    # Your Code Refactored
    # @pytest.mark.django_db
    def test_list_patient(self):
        self.client.login(username=self.username, password=self.password)

        patient1 = Patient(FullName ="TestUser 1",Date = date.today())
        patient1.save()
        patient2 = Patient(FullName ="TestUser 2",Date = date.today())
        patient2.save()

        print('list : ',reverse('Patient:List', kwargs={'PatientType': 0}))
        
        # using the client, self.client, make the POST request
        response = self.client.get(reverse('Patient:List', kwargs={'PatientType': 0}))

        self.assertContains(response,"TestUser 1")
        # self.assertContains(response,"TestUser 2")
      

    def test_add_patient(self):
        
        patient_data =  {
                'FullName' : "TestUser 1",
                'Date' : date.today(),
                'AirforceType' : 1,
                'RightMedicalTreatment' : 1,
                'CurrentStatus' : 0,
                'CurrentTreatment' : 0

        }
        # Login the client in the test
        self.client.login(username=self.username, password=self.password)

        print('abc')
        
        # using the client, self.client, make the POST request
        response = self.client.post(reverse('Patient:AddNew'), data = patient_data)

        # Get the data from the object FAIL HERE
        self.assertTrue (Patient.objects.all().count())
        
        # Assertion tests
        # self.assertEqual(patient.FullName, "TestUser 1")
        # self.assertEqual(patient.count(), 1)
        # self.assertEqual(patient.DataUser, self.user)

    
        # LoginUser = login_user();
        # client.force_login(LoginUser)
        # patient = Patient
        # assert patient.objects.count() == 0
        # AddNewPatientURL = urls.reverse('Patient:AddNew')
        # resp = client.post(AddNewPatientURL, patient_data)