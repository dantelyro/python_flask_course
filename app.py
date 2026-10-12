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
  new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', '',), completed=data.get('completed'))
  task_id_control += 1
  tasks.append(new_task)
  return jsonify({"message": "nova tarefa criada com sucesso"})

if __name__ == "__main__":
  app.run(debug=True)