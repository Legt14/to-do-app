from flask import Flask, render_template, redirect, session, url_for, request
from flask_login import login_required, current_user

from flaskr import create_app
from flaskr.forms import CreateTask, Register, Login
from flaskr.crud import get_user, get_user_tasks

app = create_app()




#2 Buttons for create task or view all task 
@app.route('/', methods=['GET'])
def root(): 
    if current_user.is_authenticated:
        user = current_user.id
        context = {
            'username': user
        }
        return render_template('home.html', **context)
    else:
        return redirect('welcome')



#Welcome to user login or register
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/tasks/create', methods=['GET', 'POST'])
@login_required
def create_task():
    create_task = CreateTask()
    context = {
        'user_id': "user_id",
        'form': create_task
    }
    return render_template('create_task.html', **context)


@app.route('/tasks/<task_id>', methods=['GET', 'POST'])
@login_required
def tasks_id(task_id):
    context = {
        'user_id': "user_id",
        'task_id': task_id,
    }
    return render_template('single_task.html', **context)




