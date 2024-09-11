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
  
def test_get_task():
  
  response = requests.get(f"{BASE_URL}/tasks")
   
  assert response.status_code == 200
  response_json = response.json()
  assert "tasks" in response_json
  assert "total_task" in response_json