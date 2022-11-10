from flask import Flask, render_template, redirect, session, url_for, request
from flask_login import login_required, current_user

from flaskr import create_app
from flaskr.forms import CreateTask, Register, Login
from flaskr.crud import get_user, get_user_tasks, task_creator

app = create_app()


#2 Buttons for create task or view all task 
@app.route('/', methods=['GET'])
def root(): 
    if current_user.is_authenticated:
        user = current_user.id
        tasks = get_user_tasks(user)
        context = {
            'username': user,
            'task': tasks
        }
        return render_template('home.html', **context)
    else:
        return redirect('welcome')


#Welcome to user login or register
@app.route('/welcome')
def welcome():
    if current_user.is_authenticated:
        user = current_user.id
        context = {
            'username': user
        }
        return render_template('welcome.html', **context)
    else:
        return render_template('welcome.html')



@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_task():
    task_form = CreateTask()
    user = current_user.id
    
    context = {
        'username': user,
        'form': task_form
    }

    if task_form.validate_on_submit():
        data = {
            'title': task_form.title.data,
            'description': task_form.task.data
        }
        print(task_creator(user_id=user, data=data))
        return redirect(url_for('root'))

    
    return render_template('create_task.html', **context)


@app.route('/<task_id>', methods=['GET', 'POST'])
@login_required
def tasks_id(task_id):
    user = current_user.id
    context = {
        'username': user,
        'task_id': task_id,
    }
    return render_template('single_task.html', **context)




