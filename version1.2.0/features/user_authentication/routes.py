from flask import render_template, request, redirect, url_for, flash
from . import dorm_allocation_bp
from .models import Dormitory
from .. import db

@dorm_allocation_bp.route('/allocate', methods=['GET', 'POST'])
def allocate_dormitory():
    if request.method == 'POST':
        # 获取表单数据
        selected_dormitory_id = request.form.get('dormitory_id')
        # TODO: 添加分配逻辑
        flash('宿舍分配成功！')
        return redirect(url_for('dorm_allocation.allocate_dormitory'))

    dormitories = Dormitory.query.all()  # 查询所有宿舍
    return render_template('allocate.html', dormitories=dormitories)
