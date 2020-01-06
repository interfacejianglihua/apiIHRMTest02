import unittest
import logging
from api.login_api import LoginApi
from utils import asser_common, read_login_daa
from parameterized.parameterized import parameterized


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

    @parameterized.expand(read_login_daa)
    def test_login(self,mobile,password,http_code,success,code,message):
        response = self.login_api.login(mobile,password)
        jsonData = response.json()
        logging.info("登录接口返回数据为:{}".format(jsonData))
        asser_common(self,response,http_code,success,code,message)


