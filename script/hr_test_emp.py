import unittest
import logging
import pymysql
from parameterized import parameterized

import app
from api.emp_api import EmpApi
from utils import asser_common, DBUtils
from utils import read_add_emp_data,read_query_emp_data,read_modify_emp_data,read_delete_emp_data


class TestEmp(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.emp_api = EmpApi()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @parameterized.expand(read_add_emp_data)
    def test01_add_emp(self, username,mobile,success,code,message,http_code):
        # 调用添加员工接口
        response = self.emp_api.add_emp(username, mobile)
        jsonData = response.json()
        logging.info("添加员工接口返回数据为:{}".format(jsonData))
        # 获取员工ID保存全局变量
        app.Emp_ID = jsonData.get("data").get("id")
        logging.info(app.Emp_ID)

        asser_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_query_emp_data)
    def test02_query_emp(self,success,code,message,http_code):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        jsonData = response.json()
        logging.info("查询员工接口的返回数据为:{}".format(jsonData))
        asser_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_modify_emp_data)
    def test03_modify_emp(self,username,success,code,message,http_code):
        # 调用修改员工接口
        response = self.emp_api.modify_emp(username)
        jsonData = response.json()
        logging.info("修改员工接口的返回数据为:{}".format(jsonData))

        # #建立连接
        # conn = pymysql.connect("182.92.81.159","readuser","iHRM_user_2019","ihrm",charset = "utf8")
        # #获取游标
        # cursor = conn.cursor()
        # #执行
        # sql = "select username from bs_user where id={}".format(app.Emp_ID)
        # cursor.execute(sql)
        # result = cursor.fetchone()[0]
        # print(result)
        # logging.info("从数据库中查询出的员工的用户名是:{}".format(result))
        # self.assertEqual(username,result)
        # #关闭游标
        # cursor.close()
        # #关闭连接
        # conn.close()

        with DBUtils() as db_utils:
            sql = "select username from bs_user where id={}".format(app.Emp_ID)
            db_utils.execute(sql)
            result = db_utils.fetchone()[0]
            logging.info("从数据库只中查询出的员工的用户名是:{}".format(result))
        #断言
        asser_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_delete_emp_data)
    def test04_delete_emp(self,success,code,message,http_code):
        # 调用删除员工接口
        response = self.emp_api.delete_emp()
        jsonData = response.json()
        logging.info("删除员工接口的返回数据为:{}".format(jsonData))
        asser_common(self, response, http_code, success, code, message)
