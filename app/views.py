from app import app
from flask import render_template, flash, redirect, url_for
from app.form import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [{'author': {'nickname': "John"}, 'body': 'Beautiful in Portugal'},
             {'author': {'nickname': 'Susan'}, 'body': 'The journey was easy'}]
    return render_template("index.html", posts=posts, user=user, title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user{}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/test', methods=['POST'])
def test():
    response={"yes":1, "no":2 }
