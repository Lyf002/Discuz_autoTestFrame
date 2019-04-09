from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
from framework.logger import Logger
import time
import random

logger=Logger(logger="HomePage").getlog()
class HomePage(BasePage):

    img_link_loc=(By.CSS_SELECTOR,".hdc h2 a img")


    # button_fatie_loc=(By.ID,"newspecial")
    # start_vote_loc=(By.CSS_SELECTOR,".mbw li:nth-last-child(1) a")
    # title_vote_loc=(By.ID,"subject")
    # option1_vote_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(1) input")
    # option2_vote_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(2) input")
    # option3_vote_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(3) input")
    # vote_content_loc=(By.CSS_SELECTOR,"body")
    # button_send_vote_loc=(By.ID,"postsubmit")
    # radio_option1=(By.CSS_SELECTOR,".pcht tbody tr:nth-child(1)  .pslt input")
    # radio_option2 = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(3)  .pslt input")
    # radio_option3 = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(5)  .pslt input")
    # radio_list=[radio_option1,radio_option2,radio_option3]
    # submit_vote_loc=(By.CSS_SELECTOR,".pn span")
    radio_title1_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(1) .pvt label")
    radio_title2_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(3) .pvt label")
    radio_title3_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(5) .pvt label")
    vote1_percent_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(2) td:nth-last-child(1)")
    vote2_percent_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(4) td:nth-last-child(1)")
    vote3_percent_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(6) td:nth-last-child(1)")
    vote_title_loc=(By.CSS_SELECTOR,".vwthd .ts span")

    #断言-----页面元素
    online_admin_loc=(By.CSS_SELECTOR,".vwmy a")
    moren_text_loc=(By.CSS_SELECTOR,".xs2 a")

    def vote_fatie(self,title,option1,option2,option3,vote_content):
        self.click(*self.button_fatie_loc)
        self.click(*self.start_vote_loc)
        self.sendkeys(title,*self.title_vote_loc)
        self.sendkeys(option1,*self.option1_vote_loc)
        self.sendkeys(option2,*self.option2_vote_loc)
        self.sendkeys(option3,*self.option3_vote_loc)
        self.driver.switch_to.frame(0)
        self.sendkeys(vote_content,*self.vote_content_loc)
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.click(*self.button_send_vote_loc)
        self.vote()
        logger.info("选项名称及投票比例：")
        title1=self.gettext(*self.radio_title1_loc)
        percent1 = self.gettext(*self.vote1_percent_loc)
        logger.info("投票选项1标题：%s"%title1)
        logger.info("投票选项1比例：%s"%percent1)
        title2 = self.gettext(*self.radio_title2_loc)
        percent2 = self.gettext(*self.vote2_percent_loc)
        logger.info("投票选项2标题：%s"%title2)
        logger.info("投票选项2比例：%s"%percent2)
        title3 = self.gettext(*self.radio_title3_loc)
        percent3 = self.gettext(*self.vote3_percent_loc)
        logger.info("投票选项3标题：%s"%title3)
        logger.info("投票选项3比例：%s"%percent3)
        mainTitle=self.gettext(*self.vote_title_loc)
        logger.info("投票标题：%s"%mainTitle)

    def vote(self):
        radiosLen=len(list(self.radio_list))
        i=random.randint(0,radiosLen-1)
        print("随机数是：",i)
        self.click(*self.radio_list[i])
        self.click(*self.submit_vote_loc)
        time.sleep(3)







