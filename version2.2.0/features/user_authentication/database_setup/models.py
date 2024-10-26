from .. import db

class Dormitory(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 宿舍ID
    name = db.Column(db.String(100), nullable=False)  # 宿舍名称
    capacity = db.Column(db.Integer, nullable=False)  # 宿舍容量
    current_occupants = db.Column(db.Integer, default=0)  # 当前入住人数

    def __repr__(self):
        return f'<Dormitory {self.name}, Capacity {self.capacity}>'
