from flask import render_template, request, redirect, url_for, flash
from . import dorm_management_bp
from .models import Dormitory
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
