from flask import render_template, session, redirect, url_for

from flaskr.forms import Login, Register
from .bp import auth



@auth.route('/login', methods=['GET', 'POST'])
def login():
    sign_in = Login()
    sign_in_session = session.get('sign_in_sesion')
    context = {
        'form': sign_in,
        'sign_in_session': sign_in_session
    }
    if sign_in.validate_on_submit():
        sign_in_session = sign_in.data #data is return data input
        session['sign_in_session'] = sign_in_session

        return redirect(url_for('root'))

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

