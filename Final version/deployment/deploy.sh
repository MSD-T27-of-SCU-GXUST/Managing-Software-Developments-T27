#!/bin/bash

# 自动化部署脚本

# 环境设置
export FLASK_APP=app.py
export FLASK_ENV=production

# 安装依赖
pip install -r requirements.txt

# 数据库迁移
flask db upgrade

# 启动应用
flask run --host=0.0.0.0 --port=5000
