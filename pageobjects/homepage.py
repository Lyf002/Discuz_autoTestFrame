from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
from framework.logger import Logger
import time
import random

logger=Logger(logger="HomePage").getlog()

class HomePage(BasePage):

    #搜索框
    input_search_loc = (By.ID, "scbar_txt")
    #搜索按钮
    button_search_loc = (By.CSS_SELECTOR, ".scbar_btn_td .pn")
    #搜索到的帖子标题
    title_link_loc = (By.CSS_SELECTOR, ".xs3 a strong font")
    #帖子标题
    title_loc = (By.ID, "thread_subject")


    #搜索帖子
    def search(self,content):
        self.clear(*self.input_search_loc)
        self.sendkeys(content,*self.input_search_loc)
        self.click(*self.button_search_loc)
        self.driver.implicitly_wait(20)
        self.driver.switch_to.window(self.driver.window_handles[1])
        webtitle = self.get_webtitle()
        return webtitle

    # 点击搜索到的帖子标题
    def title_click(self):
        self.click(*self.title_link_loc)
        self.driver.implicitly_wait(10)
        self.driver.switch_to.window(self.driver.window_handles[2])
        webtitle = self.get_webtitle()
        return webtitle