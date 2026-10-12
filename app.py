
from flask import Flask, jsonify, request

from models.task import Task

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world"


tasks = []
task_id_control = 1


@app.route('/task', methods=['POST'])
def create_task():
    global task_id_control
    id = task_id_control
    data = request.get_json()
    new_task = Task(id=id,
                    title=data['title'],
                    description=data['description']
                    )
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "nova tarefa criada com sucesso", "id": id})


@app.route('/tasks', methods=['GET'])
def list_tasks():
    task_list = [task.to_dict() for task in tasks]
    return jsonify({"tasks": task_list, "total": len(task_list)})


@app.route('/task/<int:id>', methods=['GET'])
def get_task(id):
    task = next((task.to_dict() for task in tasks if task.id == id), None)

    if task is None:
        return jsonify({"message": "Not found"}), 404

    return jsonify({"task": task})


@app.route('/task/<int:id>', methods=['PUT'])
def update(id):
    task = next((task for task in tasks if task.id == id), None)

    if task is None:
        return jsonify({"message": "Not found"}), 404

    data = request.get_json()
    task.title = data["title"]
    task.description = data['description']
    task.completed = data['completed']

    return jsonify({"message": "task updated!"})


@app.route('/task/<int:id>', methods=['DELETE'])
def delete(id):
    task = next((task for task in tasks if task.id == id), None)

    if task is None:
        return jsonify({"message": "Not found"}), 404

    tasks.remove(task)

    return jsonify({"message": "task deleted!"})


if __name__ == "__main__":
    app.run(debug=True)
