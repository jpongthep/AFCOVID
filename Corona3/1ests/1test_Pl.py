import pytest
from django.urls import reverse

def test_anonymous_views(client):
  

    temp_url = reverse('Corona3:BasicForm')
    resp = client.get(temp_url)
    assert resp.status_code == 200
def test_Corona3Form(client):
    response = client.get('/CRN3/BasicData/')
    assert "Corona3" in str(response.content)

def test_minDataForm(client):
    response = client.get('/CRN3/minData/')
    assert "" in str(response.content)

def test_modelscorona3_views(client):
  

    temp_url = reverse('Corona3:minForm')
    resp = client.get(temp_url)
    assert resp.status_code == 200

    