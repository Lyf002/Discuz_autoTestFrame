from testcase.basetestcase import BaseTestCase
from pageobjects.homepage import HomePage
from pageobjects.login_page import loginPage
from pageobjects.base import BasePage
from framework.logger import Logger
import time

logger=Logger(logger="Flow3").getlog()
class Flow3(BaseTestCase):

    def test_flow3(self):
        """
        Discuz业务流程三
        :return:
        """
        # 1.admin登录论坛
        login_page = loginPage(self.driver)
        login_page.login("admin", "lyf2580")
        login_page.click_login()
        time.sleep(3)
        # 判断admin是否登录成功
        admin_online_text = login_page.gettext(*login_page.online_admin_loc)
        try:
            self.assertEqual(admin_online_text, "admin")
            logger.info("admin用户登录成功")
        except AssertionError as AE:
            logger.error("admin用户登录失败")
            raise AE

        #2.进行帖子搜索
        home_page=HomePage(self.driver)
        home_page.search("haotest")
        base_page=BasePage(self.driver)
        search_page_title = base_page.get_webtitle()
        try:
            self.assertEqual(search_page_title, "搜索 - Discuz! Board - Powered by Discuz!")
            logger.info("%s页面跳转成功" % search_page_title)
        except AssertionError as AE:
            logger.error("%s页面跳转失败" % search_page_title)
            raise AE

        #3.进入搜索的帖子
        title_click_page_title = home_page.title_click()
        try:
            self.assertEqual(title_click_page_title, "haotest - 默认版块 - Discuz! Board - Powered by Discuz!")
            logger.info("%s页面跳转成功" % title_click_page_title)
        except AssertionError as AE:
            logger.error("%s页面跳转失败" % title_click_page_title)
            raise AE

        #4.验证帖子标题和期望的一致
        result = base_page.gettext(*home_page.title_loc)
        try:
            self.assertEqual(result, "haotest")
            logger.info("帖子搜索成功")
        except AssertionError as AE:
            logger.error("帖子搜索失败")
            raise AE

        #用户退出
        self.driver.switch_to.window(self.driver.window_handles[2])
        login_page.click_logout()

