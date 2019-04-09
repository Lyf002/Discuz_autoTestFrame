# import sys
# sys.path.append('D:/自动化测试/py_workspace/Discuz_autoTestFrame')
from testcase.basetestcase import BaseTestCase
from framework.logger import Logger
from pageobjects.base import BasePage
from pageobjects.login_page import loginPage
from pageobjects.moren_page import SendTiePage
from pageobjects.moren_page import BackTiePage
import time

logger=Logger(logger="Flow1").getlog()
class Flow1(BaseTestCase):

    def test_flow1(self):
        """
        Discuz业务流程一
        :return:
        """
        #声明HomePage对象
        login_page=loginPage(self.driver)

        #1.admin登录论坛
        login_page.login("admin","lyf2580")
        login_page.click_login()
        time.sleep(3)

        #判断admin是否登录成功
        admin_online_text = login_page.gettext(*login_page.online_admin_loc)
        try:
            self.assertEqual(admin_online_text, "admin")
            logger.info("admin用户登录成功")
        except AssertionError as AE:
            logger.error("admin用户登录失败")
            raise AE

        #2.默认板块发帖
        send_page=SendTiePage(self.driver)
        send_page.click_moren()
        send_page.contentInput("我是发帖内容！！！", "我是发帖标题！！！")
        send_page.click_fatie()

        #3.默认板块回帖
        back_page=BackTiePage(self.driver)
        back_page.backtie("我在这边回帖！！！")


        #4.admin退出论坛
        login_page.click_logout()

        #断言是否登出成功
        base_page=BasePage(self.driver)
        index_page_title = base_page.get_webtitle()
        try:
            self.assertEqual(index_page_title, "提示信息 - Discuz! Board - Powered by Discuz!")
            logger.info("admin用户退出成功")
        except AssertionError as AE:
            logger.error("admin用户退出失败")
            raise AE





