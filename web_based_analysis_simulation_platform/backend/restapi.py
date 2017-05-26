#!/usr/bin/env python3
from flask import Flask, request, jsonify
# from algorithm import approx
from worker import integrate

# http GET http://localhost:5000
# http GET http://localhost:5000/0
# http GET http://localhost:5000/1
# http PUT http://localhost:5000 (next line)
# f='sqrt(4 - xs**2)' a:=0 b:=2 c:=0 d:=2 size:=10000
app = Flask(__name__)
TASKS = {}

@app.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = TASKS.get(task_id)
    if task and task.ready():
        response = {task_id: task.get(timeout=1)}
    else:
        response = {task_id: 'still working...'}
    return jsonify(response)

@app.route('/', methods=['GET'])
def list_task():
    tasks = {task_id: {'ready': task.ready()}
             for task_id, task in TASKS.items()}
    return jsonify(tasks)

@app.route('/', methods=['PUT'])
def put_task():
    f = request.json['f']
    a = request.json['a']
    b = request.json['b']
    c = request.json['c']
    d = request.json['d']
    size = request.json.get('size', 100)

    # response = {
    #     'result': approx(f, a, b, c, d, size),
    # }

    task_id = len(TASKS)
    TASKS[task_id] = integrate.delay(f, a, b, c, d, size)
    response = {'result': task_id}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
