from flask import render_template, session, redirect, url_for, flash
from flask_login import login_user

from flaskr.forms import Login, Register
from flaskr.crud import get_user
from flaskr.models import UserData, UserModel

from .bp import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = Login()
    login_in_session = session.get('sign_in_sesion')
    context = {
        'form': login_form,
        'login _in_session': login_in_session
    }
    if login_form.validate_on_submit():
        username = login_form.username.data #data is return data input
        password = login_form.password.data

        user_doc = get_user(username)
        
        if user_doc.to_dict() is not None:
            user_password = user_doc.to_dict()['password']

            if user_password == password:
                user_data = UserData(username, password)
                user = UserModel(user_data)

                login_user(user)

                return redirect(url_for('root'))

            else:
                flash('Password incorrect')
    
        else:
            flash('User no exist')
        
    
    return render_template('login.html', **context)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    register = Register()
    register_session = session.get('register')
    context = {
        'form': register,
        'register': register_session
    }
    
    if register.validate_on_submit():
        register_session = register.data #data is return data input
        session['register'] = register_session

        return redirect(url_for('root'))

    return render_template('register.html', **context)

