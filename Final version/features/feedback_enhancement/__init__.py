from flask import Blueprint

feedback_enhancement_bp = Blueprint('feedback_enhancement', __name__)

from . import routes  # 导入路由文件
