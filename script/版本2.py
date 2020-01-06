import unittest
import logging

import app
from api.emp_api import EmpApi
from utils import asser_common

from api.login_api import LoginApi




class TestEmp(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.emp_api = EmpApi()
        cls.login_api = LoginApi()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):

        pass

    def test01_login(self):
        response = self.login_api.login("13800000002", "123456")
        jsonData = response.json()
        logging.info("登录成功接口返回数据为:{}".format(jsonData))

        asser_common(self, response, 200, True, 10000, "操作成功")
        token = jsonData.get("data")
        app.HEADERS["Authorization"] = "Bearer " + token
        logging.info("保存的令牌是:{}".format(app.HEADERS))

    def test02_add_emp(self):
        response = self.emp_api.add_emp("小五","299999111888")
        jsonData = response.json()
        logging.info("添加员工接口返回数据为:{}".format(jsonData))
        asser_common(self,response,200,True,10000,"操作成功")

        #获取员工ID保存全局变量
        app.Emp_ID = jsonData.get("data").get("id")