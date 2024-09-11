from flask import Flask, jsonify, request
from model.task import Task

app = Flask(__name__)

tasks = []
task_id=1

@app.route('/tasks',methods=['POST'])
def create_task():
  global task_id
  data = request.get_json()
  new_task = Task(id=task_id,title=data['title'],description=data['description'])
  task_id +=1
  tasks.append(new_task)
  return jsonify(new_task.to_dict()), 200

@app.route('/tasks', methods=['GET'])
def get_task():
  
  task_list = [task.to_dict() for task in tasks]

  output = {
    "tasks":task_list,
    "total_task":len(task_list)
  }
  return jsonify(output)


@app.route('/tasks/<int:id>', methods=['GET'])
def get_taskId(id):
  for task in tasks:
    if task.id == id:
      return jsonify(task.to_dict())
    
  return jsonify({"message":"Não foi encontrado!"}), 404
  
if __name__ == "__main__":
  app.run(debug=True)