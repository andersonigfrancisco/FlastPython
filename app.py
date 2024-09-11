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
  print(tasks)
  return "teste"

@app.route('/tasks', methods=['GET'])
def get_task():
  
  task_list = [Task.to_dict() for Task in tasks]

  output = {
    "tasks":task_list,
    "total_task":""
  }
  return jsonify(output)
  
if __name__ == "__main__":
  app.run(debug=True)