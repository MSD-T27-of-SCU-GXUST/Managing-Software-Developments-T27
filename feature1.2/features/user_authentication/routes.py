from flask import Blueprint, render_template, request, redirect, url_for
from .forms import LoginForm, RegistrationForm
from features.database_setup.models import User, db

user_authentication_bp = Blueprint('user_authentication', __name__)

@user_authentication_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 登录逻辑
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            # 登录成功逻辑
            return redirect(url_for('dashboard'))  # 假设有一个仪表板
    return render_template('login.html', form=form)

@user_authentication_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # 注册逻辑
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_authentication.login'))
    return render_template('register.html', form=form)
