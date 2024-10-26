from flask import render_template, redirect, url_for, flash
from . import allocation_optimization_bp
from ..models import Dormitory, Student  # 假设有 Student 模型
from .. import db

@allocation_optimization_bp.route('/optimize', methods=['GET', 'POST'])
def optimize_allocation():
    if request.method == 'POST':
        # 获取所有学生和宿舍信息
        students = Student.query.all()
        dormitories = Dormitory.query.all()
        
        # 假设有一个优化算法函数 optimize_dorm_allocation
        allocation_result = optimize_dorm_allocation(students, dormitories)
        
        # 在这里可以将分配结果保存到数据库或返回给前端
        flash('宿舍分配已优化！')
        return redirect(url_for('allocation_optimization.optimize_allocation'))

    return render_template('optimize.html')
