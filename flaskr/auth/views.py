from flask import render_template, session, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from flaskr.forms import Login, Register
from flaskr.crud import get_user, get_emial, user_register
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

            if check_password_hash(user_password, password):
                user_data = UserData(username, password)
                user = UserModel(user_data)

                login_user(user)

                return redirect(url_for('welcome'))

            else:
                flash('Password incorrect')
    
        else:
            flash('User no exist')
        
    
    return render_template('login.html', **context)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    register = Register()
    context = {
        'form': register,
    }
    
    username = register.username.data
    email = register.email.data
    password = register.password.data
    
    if register.validate_on_submit():
        if get_user(username) or get_emial(email) is None:
            hash_pwd = generate_password_hash(password)
            data = {
                'username': username,
                'email': email,
                'password': hash_pwd
            }

            user_data = UserData(username, hash_pwd)
            user = UserModel(user_data)
            user_register(username, data)
            login_user(user)
            return redirect(url_for('welcome'))

        else:
            flash('The Username or Email already exist'.format(username))


    return render_template('register.html', **context)


@auth.route('/logout')
@login_required
def logout():
    flash('See you later')
    logout_user()

    return redirect(url_for('auth.login'))