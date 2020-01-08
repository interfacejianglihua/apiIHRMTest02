import unittest
import time

from app import BASE_DIR
from script.hr_login import Login
from script.hr_test_emp import TestEmp
from script.hr_test_login import TestIHRMLogin
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(Login)) #导入登录员工和员工管理
suite.addTest(unittest.makeSuite(TestEmp))
# suite.addTest(unittest.makeSuite(TestIHRMLogin))

#report_path = BASE_DIR + "/report/ihrm{}.html".format(time.strftime("%Y%m%d_%H%M%S"))
report_path = BASE_DIR + "/report/ihrm.html"

with open(report_path,"wb") as f:
    runner = HTMLTestRunner(f,verbosity=1,title="自动化接口测试",description="v1.0")
    runner.run(suite)
