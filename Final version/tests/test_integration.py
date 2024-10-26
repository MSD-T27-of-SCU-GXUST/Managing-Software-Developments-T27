import unittest
from app import app, db, models

class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_registration(self):
        response = self.app.post('/register', data=dict(
            username='testuser',
            password='testpass'
        ))
        self.assertEqual(response.status_code, 302)  # 重定向
        self.assertIn(b'注册成功', response.data) 

    def test_user_login(self):
        self.app.post('/register', data=dict(
            username='testuser',
            password='testpass'
        ))
        response = self.app.post('/login', data=dict(
            username='testuser',
            password='testpass'
        ))
        self.assertEqual(response.status_code, 302)  # 重定向
        self.assertIn(b'登录成功', response.data) 

# 其他测试用例...
