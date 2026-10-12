import requests

BASE_URL = 'http://localhost:5000'
task_id = 0


def test_create_task():
    global task_id
    new_task_data = {
        "title": "test title",
        "description": "test description"
    }
    response = requests.post(f"{BASE_URL}/task", json=new_task_data)
    response_json = response.json()
    assert response.status_code == 200
    assert "message" in response_json
    assert "id" in response_json
    task_id = response_json["id"]


def test_list_task():
    response = requests.get(f"{BASE_URL}/tasks")
    response_json = response.json()
    assert response.status_code == 200
    assert "tasks" in response_json
    assert response_json["total"] == 1


def test_get_task():
    response = requests.get(f"{BASE_URL}/task/{task_id}")
    response_json = response.json()
    assert response.status_code == 200
    assert "task" in response_json
    assert response_json['task']["title"] == 'test title'
    assert response_json['task']["description"] == 'test description'
    assert response_json['task']["completed"] == False


def test_put_task():
    new_task_data = {
        "title": "test update",
        "description": "test update",
        "completed": True
    }
    response = requests.put(f"{BASE_URL}/task/{task_id}", json=new_task_data)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['message'] == 'task updated!'


def test_delete_task():
    response = requests.delete(f"{BASE_URL}/task/{task_id}")
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['message'] == 'task deleted!'
