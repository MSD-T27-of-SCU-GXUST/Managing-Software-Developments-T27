from flask import Blueprint

allocation_optimization_bp = Blueprint('allocation_optimization', __name__)

from . import routes  # 导入路由文件
