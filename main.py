from flask import Flask, render_template, redirect, session, url_for, request
from flask_login import login_required

from flaskr import create_app
from flaskr.forms import CreateTask, Register, Login
from flaskr.crud import get_users, get_user_tasks
from flaskr.models import User

app = create_app()


#2 Buttons for create task or view all task 
@app.route('/', methods=['GET'])
@login_required
def root():
    #Make a validations to view home if user is logget else redirect to welcomen
    users = get_users()
    context = {
        'users': users
    }
    for record in users:
        user_id = record.id
        print(user_id)
        tasks = get_user_tasks(user_id)
        print(tasks)
            

    return render_template('home.html')


#Welcome to user login or register
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/user/<id_user>')
@login_required
def user(id_user):
    context = {
        'id_user': id_user
    }
    return render_template('user.html', **context)


@app.route('/user/<user_id>/tasks', methods=['GET', 'POST'])
@login_required
def tasks(user_id):
    return render_template('tasks.html')


@app.route('/user/<user_id>/tasks/create', methods=['GET', 'POST'])
@login_required
def create_task(user_id):
    create_task = CreateTask()
    context = {
        'user_id': user_id,
        'form': create_task
    }
    return render_template('create_task.html', **context)


@app.route('/user/<user_id>/tasks/<task_id>', methods=['GET', 'POST'])
@login_required
def tasks_id(user_id, task_id):
    context = {
        'user_id': user_id,
        'task_id': task_id,
    }
    return render_template('single_task.html', **context)




