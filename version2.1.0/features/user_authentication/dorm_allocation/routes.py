from flask import render_template, request, redirect, url_for, flash
from . import dorm_management_bp
from . import user_feedback_bp
from .models import Dormitory
from .models import Feedback
from .. import db

@dorm_management_bp.route('/manage', methods=['GET', 'POST'])
def manage_dormitories():
    if request.method == 'POST':
        # 获取表单数据
        dormitory_name = request.form.get('name')
        dormitory_capacity = request.form.get('capacity')
        new_dormitory = Dormitory(name=dormitory_name, capacity=dormitory_capacity)
        
        db.session.add(new_dormitory)  # 添加新宿舍
        db.session.commit()  # 提交到数据库
        flash('宿舍添加成功！')
        return redirect(url_for('dorm_management.manage_dormitories'))

    dormitories = Dormitory.query.all()  # 查询所有宿舍
    return render_template('manage.html', dormitories=dormitories)

@user_feedback_bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # 获取表单数据
        user_name = request.form.get('name')
        user_message = request.form.get('message')
        new_feedback = Feedback(name=user_name, message=user_message)
        
        db.session.add(new_feedback)  # 添加新反馈
        db.session.commit()  # 提交到数据库
        flash('反馈提交成功！')
        return redirect(url_for('user_feedback.feedback'))

    feedbacks = Feedback.query.all()  # 查询所有反馈
    return render_template('feedback.html', feedbacks=feedbacks)