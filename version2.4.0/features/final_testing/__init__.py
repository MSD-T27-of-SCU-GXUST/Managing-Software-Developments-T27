from flask import Blueprint

final_testing_bp = Blueprint('final_testing', __name__)

from . import routes  # 导入路由文件
