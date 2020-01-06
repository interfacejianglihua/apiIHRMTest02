import unittest
import logging

from api.login_api import LoginApi
from utils import asser_common

class TestIHRMLogin(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test01_login_success(self):
        response = self.login_api.login("13800000002","123456")
        jsonData = response.json()
        logging.info("登录成功接口返回数据为:{}".format(jsonData))
        #断言
        # self.assertEqual(200,response.status_code)
        # self.assertEqual(True,jsonData.get("success"))
        # self.assertEqual(10000,jsonData.get("code"))
        # self.assertIn("操作成功",jsonData.get("message"))
        asser_common(self,response,200,True,10000,"操作成功")

    def test02_username_is_not_exists(self):
        response = self.login_api.login("13900000002","123456")
        jsonData = response.json()
        logging.info("账号不存在时输入的数据为:{}".format(jsonData))
        asser_common(self,response,200,False,20001,"用户名或密码错误")

    def test03_password_error(self):
        response = self.login_api.login("13800000002", "error")
        jsonData = response.json()
        logging.info("密码错误时输入的数据为:{}".format(jsonData))
        asser_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test04_username_have_special_char(self):
        response = self.login_api.login("@!%$&@+-", "123456")
        jsonData = response.json()
        logging.info("账号有特殊字符时输入的数据为:{}".format(jsonData))
        asser_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test05_username_is_empty(self):
        response = self.login_api.login(" ", "error")
        jsonData = response.json()
        logging.info("账号为空时输入的数据为:{}".format(jsonData))
        asser_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test06_password_is_empty(self):
        response = self.login_api.login("13800000002", " ")
        jsonData = response.json()
        logging.info("密码为空时输入的数据为:{}".format(jsonData))
        asser_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test07_username_have_chinese(self):
        response = self.login_api.login("13800中文000002", "123456")
        jsonData = response.json()
        logging.info("账号有中文时输入的数据为:{}".format(jsonData))
        asser_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test08_username_have_space(self):
        response = self.login_api.login("138000 00002", "123456")
        jsonData = response.json()
        logging.info("账号有空格时输入的数据为:{}".format(jsonData))
        asser_common(self, response, 200, False, 20001, "用户名或密码错误")

