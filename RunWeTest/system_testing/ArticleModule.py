import unittest
import requests
from BeautifulReport import BeautifulReport

suite = unittest.TestSuite()    # 类的实例化！！！要加括号才是实例化


class ArticleTest(unittest.TestCase):  # 调用unittest
    def setUp(self) -> None:  # 前置条件
        # 登录接口
        re = requests.post(url='http://localhost:8081/Login',
                           data={'password': '123456', 'phone': '16696738903'})  # 发送接口请求
        global token  # 设置一个全局变量
        token = re.json()['data']['tokenValue']  # 给全局变量赋值，值为接口响应的token的值

    def tearDown(self) -> None:          # 后置条件
        print("执行结束")  # 打印标示用例执行结束

    def test_add_article(self):
        '''
        添加文章
        '''
        res = requests.post('http://localhost:8081/article/',
                            headers={
                                'Content-Type': 'application/json', "satoken": token},
                            params={"context": "hello world!"})
        a = res.text
        print(a)

    def test_get_article(self):
        '''
        获取文章
        '''
        res = requests.get('http://localhost:8081/article/'+'35',
                           headers={'Content-Type': 'application/json', "satoken": token})
        a = res.text
        print(a)  # 打印结果

    def test_like(self):
        '''
        点赞文章
        '''
        payload = {"user_id": 29, "id": 35}
        print(payload)
        res = requests.put('http://localhost:8081/article/like2/',
                           params=payload)
        a = res.text
        print(a)

    def test_unlike(self):
        '''
        取消点赞文章
        '''
        payload = {"user_id": 29, "id": 35}
        print(payload)
        res = requests.put('http://localhost:8081/article/like2/',
                           params=payload)
        a = res.text
        print(a)


if __name__ == '__main__':
    suite.addTest(ArticleTest('test_add_article'))  # 添加测试用例
    suite.addTest(ArticleTest('test_get_article'))  # 添加测试用例
    suite.addTest(ArticleTest('test_like'))  # 添加测试用例
    suite.addTest(ArticleTest('test_unlike'))  # 添加测试用例
    # 添加用例描述
    result = BeautifulReport(suite)
    result.report(filename='Article系统测试报告', description='Article系统测试报告',
                  log_path='./report')
    # unittest.main()
