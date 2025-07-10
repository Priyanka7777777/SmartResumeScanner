from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.forms.login_form import LoginForm
from app.forms.register_form import RegisterForm
from app.models.user import User, db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    return render_template('index.html')


# Register route
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered', 'warning')
            return redirect(url_for('auth.register'))

        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(email=form.email.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html', form=form)

# Login route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html', form=form)

# Dashboard route
@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.email)


# Logout route
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('auth.index'))
