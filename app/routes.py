from flask import render_template, flash, redirect, url_for, request
from app import app
from app import db
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.models import User,UsbMemory
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from werkzeug.urls import url_parse

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == "GET":
        usbMemorys = UsbMemory.query.all()
        return render_template("index.html", title='Home Page', usbMemorys = usbMemorys)
    else: # POST
        if "loan" in request.form: # 貸出
            usbMemory = UsbMemory.query.filter_by(usb_number=request.form["loan"]).first()
            usbMemory.user_id = current_user.id
            db.session.add(usbMemory)
            db.session.commit()
        #elif "ret" in request.form:  返却
        usbMemorys = UsbMemory.query.all()
        return render_template("index.html", title='Home Page', usbMemorys = usbMemorys)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=form.userId.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=form.userId.data).first()
        if user is None: # user_idが存在しない場合登録可能
            user = User(id=form.userId.data,username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        else:
            flash('This ID already exists')
            return render_template('register.html', title='Register', form=form)
    return render_template('register.html', title='Register', form=form)
