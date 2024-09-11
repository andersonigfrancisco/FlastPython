import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

task = []

def test_create_task():
  new_data_task = {
    "title":"title1",
    "description":"description",
    "completed": False
  }
  response = requests.post(f"{BASE_URL}/tasks",json=new_data_task) 
  assert response.status_code == 200
  response_json = response.json()
  assert "id" in response_json
  assert response_json['id']==1