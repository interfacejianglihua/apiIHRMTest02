import unittest
import logging
from api.login_api import LoginApi
from app import HEADERS
from utils import asser_common
class Login(unittest.TestCase):
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

    def test_login(self):
        response = self.login_api.login("13800000002","123456")
        jsonData = response.json()
        logging.info("登录成功接口返回数据为:{}".format(jsonData))

        asser_common(self,response,200,True,10000,"操作成功")
        token = jsonData.get("data")
        HEADERS["Authorization"] = "Bearer " + token
        logging.info("保存的令牌是:{}".format(HEADERS))



