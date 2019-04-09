from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
from framework.logger import Logger

logger=Logger(logger="SendTiePage").getlog()
#发帖
class SendTiePage(BasePage):

    #默认板块
    moren_link_loc = (By.CSS_SELECTOR, ".bm_c h2 a")
    #发帖内容、发帖标题输入框
    input_content_loc = (By.CSS_SELECTOR, ".bm_c .pbt input")
    input_title_loc = (By.ID, "fastpostmessage")

    #发帖按钮
    button_submit_loc = (By.ID, "fastpostsubmit")

    #点击默认板块
    def click_moren(self):
        self.click(*self.moren_link_loc)

    #输入发帖内容
    def contentInput(self, content, title):
        self.sendkeys(content, *self.input_content_loc)
        self.sendkeys(title, *self.input_title_loc)

    def click_fatie(self):
        self.click(*self.button_submit_loc)


#回帖
class BackTiePage(BasePage):

    #回帖输入框
    input_huitie_loc = (By.ID, "fastpostmessage")

    #输入回帖内容
    def backtie(self,content):
        self.sendkeys(content, *self.input_huitie_loc)

#删帖
class DelTiePage(BasePage):
    #帖子选择框
    check_box_loc = (By.NAME, "moderate[]")
    #删除按钮
    button_del_loc = (By.LINK_TEXT, "删除")
    #确认删除按钮
    button_sure_loc = (By.ID, "modsubmit")


    #删除帖子操作
    def del_tie(self):
        self.click(*self.check_box_loc)
        self.click(*self.button_del_loc)
        self.click(*self.button_sure_loc)


