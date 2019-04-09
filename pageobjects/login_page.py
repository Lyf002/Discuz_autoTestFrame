from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
import time

class loginPage(BasePage):
    #用户名、密码输入框
    input_username_loc = (By.ID, "ls_username")
    input_password_loc = (By.ID, "ls_password")
    #登录按钮
    button_login_loc = (By.CSS_SELECTOR, ".fastlg_l em")
    #取当前登录用户名
    online_admin_loc = (By.CSS_SELECTOR, ".vwmy a")
    # 退出按钮
    button_logout_loc = (By.LINK_TEXT, "退出")


    #输入用户名、密码
    def login(self,uname,upwd):
        self.sendkeys(uname,*self.input_username_loc)
        self.sendkeys(upwd, *self.input_password_loc)

    #点击登录按钮
    def click_login(self):
        self.click(*self.button_login_loc)
        time.sleep(5)
        webtitle=self.get_webtitle()
        return webtitle

    #点击退出按钮
    def click_logout(self):
        self.click(*self.button_logout_loc)
        webtitle = self.get_webtitle()
        return webtitle


