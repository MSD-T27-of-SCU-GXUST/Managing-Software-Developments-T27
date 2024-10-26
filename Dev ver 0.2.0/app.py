from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from features.user_authentication.routes import user_authentication_bp
from features.database_setup.models import db

app = Flask(__name__)
app.config.from_object(Config)

# 初始化数据库
db.init_app(app)

# 注册蓝图
app.register_blueprint(user_authentication_bp, url_prefix='/auth')

# 创建数据库和表
with app.app_context():
    db.create_all()  # 创建所有表

if __name__ == '__main__':
    app.run(debug=True)
