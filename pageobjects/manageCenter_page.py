from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
from framework.logger import Logger
import time

logger=Logger(logger="ManagePage").getlog()
class ManagePage(BasePage):

    #管理中心按钮
    manage_center_loc = (By.LINK_TEXT, "管理中心")
    #管理员密码框
    manage_login_pwd_loc = (By.NAME, "admin_password")
    #登录按钮
    button_manage_login_loc = (By.NAME, "submit")
    #论坛链接
    luntan_link_loc = (By.ID, "header_forum")
    # 新建板块按钮
    add_newBankuai_loc = (By.CSS_SELECTOR, ".lastboard .addtr")
    #新建板块名称输入框
    input_bkname_loc = (By.NAME, "newforum[1][]")
    #提交新版块按钮
    submit_editsubmit_loc = (By.ID, "submit_editsubmit")
    #管理中心退出按钮
    mamager_logout_loc = (By.CSS_SELECTOR, ".uinfo p a")
    #新建板块
    new_part_link_loc = (By.CSS_SELECTOR, ".fl_tb tbody tr:nth-last-child(2) td:nth-last-child(3) h2 a")


    #点击管理中心
    def click_manageCenter(self):
        self.click(*self.manage_center_loc)
        # self.driver.implicitly_wait(10)

    #切换窗口
    def change_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def manaCenter_Login(self,password):
        self.sendkeys(password, *self.manage_login_pwd_loc)
        self.click(*self.button_manage_login_loc)

    def IsLoginSuccess(self):
        try:
            # assert "登录管理中心" in self.driver.title
            #激活新窗口
            self.change_window()
            logger.info("Switch to current window successfully")
            self.manaCenter_Login("lyf2580")
            self.click(*self.button_manage_login_loc)
            self.driver.implicitly_wait(10)
            webtitle = self.get_webtitle()
            return webtitle
        except Exception as e:
            logger.error("Failed to switch to current window.")

    def click_luntan(self):
        self.click(*self.luntan_link_loc)
        self.driver.implicitly_wait(10)


    def add_new_part(self,bk_name):

        #激活iframe
        self.driver.switch_to.frame(0)
        self.click(*self.add_newBankuai_loc)

    #退出管理中心
    def logout(self):
        self.change_window()
        self.click(*self.mamager_logout_loc)

    #点击新添版块
    def click_newpart(self):
        self.click(*self.new_part_link_loc)


