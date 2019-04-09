import sys
sys.path.append('D:/自动化测试/py_workspace/Discuz_autoTestFrame')

from testcase.Discuz_test1 import Flow1
from testcase.Discuz_test2 import Flow2
from testcase.Discuz_test3 import Flow3
from testcase.Discuz_test4 import Flow4
import unittest
import HTMLTestRunner
import os
import time

# 设置报告文件保存路径
repoter_path = os.path.dirname(os.path.abspath('.'))+ '/Discuz_autoTestFrame/repoter/'
print("+++++++++++++++++",repoter_path)
# if not os.path.exists(repoter_path):
# #     os.mkdir(repoter_path)
now=time.strftime(('%Y-%m-%d-%H_%M_%S'),time.localtime(time.time()))
html_repoter = repoter_path +now+"_result.html"
# fp = open(html_repoter, "wb")

# 构造测试套件

#方法一
suite = unittest.TestSuite()
suite.addTest(Flow1('test_flow1'))
suite.addTest(Flow2('test_flow2'))
suite.addTest(Flow3('test_flow3'))
suite.addTest(Flow4('test_flow4'))

#方法二：通过makeSuite把整个class的测试case都加入套件中
# suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(Flow1))
# suite.addTest(unittest.makeSuite(Flow2))
# suite.addTest(unittest.makeSuite(Flow3))
# suite.addTest(unittest.makeSuite(Flow4))

#方法三：通过discover把整个package的所有测试case都加入套件中
# suite=unittest.TestLoader().discover("testsuites")

if __name__ == "__main__":
    fp = open(html_repoter, "wb")
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="单元测试报告", description="用例执行情况")
    runner.run(suite)
    fp.close()
