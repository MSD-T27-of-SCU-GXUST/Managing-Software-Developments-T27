from flask import Blueprint

dorm_allocation_bp = Blueprint('dorm_allocation', __name__)

from . import routes  # 导入路由文件
