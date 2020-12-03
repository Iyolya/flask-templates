from app import app
from flask import render_template, request
from app.models.todo_list import tasks, add_new_task
from app.models.task import *
@app.route('/')
def index():
    return render_template("index.html", title="Home ", tasks=tasks)
                    #1st arg. here is the name of the file
                    #3rd we want to pass the value that tasks passes in

@app.route('/add-task', methods=['POST'])
def add_task():
    task_title = request.form['title']
    task_desc = request.form['description']
    new_task = Task(task_title, task_desc, False)
    add_new_task(new_task)
    return render_template('index.html', title='Home', tasks=tasks)