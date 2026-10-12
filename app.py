
from flask import Flask, jsonify, request

from models.task import Task

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello world"

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', '',))
  task_id_control += 1
  tasks.append(new_task)
  return jsonify({"message": "nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def list_tasks():
  task_list = [task.to_dict() for task in tasks]
  return jsonify({ "tasks": task_list, "total": len(task_list) })

@app.route('/task/<int:id>', methods=['GET'])
def get_task(id):
  task = next((task.to_dict() for task in tasks if task.id == id), None)

  if task is None:
    return jsonify({"message": "Not found"})

  return jsonify({ "task": task }), 404

@app.route('/task/<int:id>', methods=['PUT'])
def update(id):
  task = next((task for task in tasks if task.id == id), None)

  if task is None:
    return jsonify({"message": "Not found"})

  data = request.get_json()

  print(data)
  task.title = data["title"]
  task.description = data['description']
  task.completed = data['completed']

  return jsonify({ "task": "task updated!" }), 404

if __name__ == "__main__":
  app.run(debug=True)