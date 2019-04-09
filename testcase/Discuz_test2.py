from testcase.basetestcase import BaseTestCase
from pageobjects.login_page import loginPage
from pageobjects.moren_page import SendTiePage
from pageobjects.moren_page import BackTiePage
from pageobjects.moren_page import DelTiePage
from pageobjects.manageCenter_page import ManagePage
from framework.logger import Logger

from pageobjects.base import BasePage
import time


class Flow2(BaseTestCase):

    def test_flow2(self):
        """
        业务流程二
        :return:
        """
        #声明HomePage对象
        login_page = loginPage(self.driver)

        # 1.admin登录论坛
        login_page.login("admin", "lyf2580")
        login_page.click_login()
        time.sleep(3)

        #2.进入默认板块删除帖子
        send_page = SendTiePage(self.driver)
        send_page.click_moren()

        del_page=DelTiePage(self.driver)
        del_page.del_tie()

        #3.进入版块管理(管理中心--论坛)
        manage_page=ManagePage(self.driver)
        manage_page.click_manageCenter()
        manage_page.change_window()
        manage_page.IsLoginSuccess()
        manage_page.click_luntan()

        #4.创建新的版块
        manage_page.add_new_part("新版块01")

        #5.管理员退出
        manage_page.logout()
        login_page.click_logout()

        #6.普通用户登录
        login_page.login("嗯哼哈呼嘿", "123456")
        login_page.click_login()

        #7.在新的版块下发帖
        manage_page.click_newpart()
        send_page = SendTiePage(self.driver)
        send_page.contentInput("我是新版块发帖内容！！！", "我是新版块发帖标题！！！")
        send_page.click_fatie()

        #8.在新的版块下回帖
        back_page = BackTiePage(self.driver)
        back_page.backtie("我在这边回帖！！！")




















        # home_page.login("admin","lyf2580")
        # homePage_webtitle=base_page.get_webtitle()
        # #判断打开论坛首页是否正确
        # self.assertEqual(homePage_webtitle,"【新提醒】论坛 - Powered by Discuz!",msg="%s页面跳转失败"%homePage_webtitle)
        #
        # home_page.moren_click()
        # home_page.del_tie()
        # #弹出登录窗口
        # home_page.manage_center("lyf2580")
        # managepage_title=base_page.get_webtitle()
        # # 判断进入管理中心页面是否正确
        # self.assertEqual(managepage_title, "Discuz! Board 管理中心 - 首页", msg="%s页面跳转失败" % managepage_title)
        #
        # home_page.add_new_part("新版块01")
        # home_page.logout2()
        # home_page.logout1()
        # home_page.login("嗯哼哈呼嘿", "123456")
        # home_page.click_new_part()
        # home_page.fatie("我是发帖内容！！！", "我是发帖标题！！！")
        # home_page.huitie("我在这边回帖！！！")