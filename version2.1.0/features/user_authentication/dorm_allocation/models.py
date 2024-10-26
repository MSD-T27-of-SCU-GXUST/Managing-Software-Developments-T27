from .. import db

class Dormitory(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 宿舍ID
    name = db.Column(db.String(100), nullable=False)  # 宿舍名称
    capacity = db.Column(db.Integer, nullable=False)  # 宿舍容量
    current_occupants = db.Column(db.Integer, default=0)  # 当前入住人数

    def __repr__(self):
        return f'<Dormitory {self.name}, Capacity {self.capacity}>'

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 反馈ID
    name = db.Column(db.String(100), nullable=False)  # 用户姓名
    message = db.Column(db.Text, nullable=False)  # 用户反馈内容

    def __repr__(self):
        return f'<Feedback {self.name}: {self.message}>'