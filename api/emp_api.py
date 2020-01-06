import requests
import app

class EmpApi:
    def __init__(self):
        self.emp_url = app.HOST + "/api/sys/user"
        self.headers = app.HEADERS

    def add_emp(self,username,mobile):
        #封装添加员工接口
        data = {"username": username,
        "mobile": mobile,
        "timeOfEntry": "2019-12-02",
        "formOfEmployment": 1,
        "workNumber": "1234",
        "departmentName": "测试",
        "departmentId": "1210411411066695680",
        "correctionTime": "2019-12-15T16:00:00.000Z"
    }
        response = requests.post(self.emp_url,json=data,headers=self.headers)
        return response

    def query_emp(self):
        #封装查询员工接口
        #http://182.92.81.159/api/sys/user/12344343221
        url = self.emp_url + "/" + app.Emp_ID
        return requests.get(url,headers = self.headers)

    def modify_emp(self,username):
        #封装修改员工接口
        url = self.emp_url + "/" + app.Emp_ID
        data = {
            "username":username
        }
        return requests.put(url,json = data,headers = self.headers)

    def delete_emp(self):
        #封装删除员工接口
        url = self.emp_url + "/" + app.Emp_ID
        return requests.delete(url,headers=self.headers)