from flask import render_template, flash, redirect
from blog import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Blog', body='hello world', \
            posts=['post1', 'post2'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login required for OpenID="%s", remember_me=%s' %
                (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
            title='Sign',
            form=form,
            providers=app.config['OPENID_PROVIDER'])
