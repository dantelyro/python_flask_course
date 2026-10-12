import requests

BASE_URL = 'http://localhost:5000'
tasks = []


def test_create_task():
    new_task_data = {
        "title": "test title",
        "description": "test description"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
