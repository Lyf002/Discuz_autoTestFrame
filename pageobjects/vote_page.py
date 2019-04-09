from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
from framework.logger import Logger
import random

logger=Logger(logger="SendTiePage").getlog()
#发起投票
class VotePage(BasePage):

    #发帖按钮
    button_fatie_loc = (By.ID, "newspecial")
    #发起投票按钮
    start_vote_loc = (By.CSS_SELECTOR, ".mbw li:nth-last-child(1) a")
    #投票标题输入框
    title_vote_loc = (By.ID, "subject")
    #投票选项
    option1_vote_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(1) input")
    option2_vote_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(2) input")
    option3_vote_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(3) input")
    #投票内容输入框
    vote_content_loc = (By.CSS_SELECTOR, "body")
    #提交投票帖子
    button_send_vote_loc = (By.ID, "postsubmit")
    #单选按钮
    radio_option1 = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(1)  .pslt input")
    radio_option2 = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(3)  .pslt input")
    radio_option3 = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(5)  .pslt input")
    radio_list = [radio_option1, radio_option2, radio_option3]
    #提交投票结果
    submit_vote_loc = (By.CSS_SELECTOR, ".pn span")
    #选项标题
    radio_title1_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(1) .pvt label")
    radio_title2_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(3) .pvt label")
    radio_title3_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(5) .pvt label")
    #选项比例
    vote1_percent_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(2) td:nth-last-child(1)")
    vote2_percent_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(4) td:nth-last-child(1)")
    vote3_percent_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(6) td:nth-last-child(1)")
    #投票标题
    vote_title_loc = (By.CSS_SELECTOR, ".vwthd .ts span")


    #点击发帖按钮
    def click_SendTie_btn(self):
        self.click(*self.button_fatie_loc)



    #发投票帖子
    def click_StartVote_btn(self):
        self.click(*self.start_vote_loc)

    def voteInfo(self,title,option1,option2,option3,vote_content):
        self.sendkeys(title, *self.title_vote_loc)
        self.sendkeys(option1, *self.option1_vote_loc)
        self.sendkeys(option2, *self.option2_vote_loc)
        self.sendkeys(option3, *self.option3_vote_loc)
        self.driver.switch_to.frame(0)
        self.sendkeys(vote_content, *self.vote_content_loc)
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.click(*self.button_send_vote_loc)

    #进行投票
    def vote(self):
        radiosLen = len(list(self.radio_list))
        i = random.randint(0, radiosLen - 1)
        print("随机数是：", i)
        self.click(*self.radio_list[i])
        self.click(*self.submit_vote_loc)

    def showVotePer(self):
        percent1 = self.gettext(*self.vote1_percent_loc)
        logger.info("投票选项1比例：%s" % percent1)
        percent2 = self.gettext(*self.vote2_percent_loc)
        logger.info("投票选项2比例：%s" % percent2)
        percent3 = self.gettext(*self.vote3_percent_loc)
        logger.info("投票选项3比例：%s" % percent3)

    def showVoteName(self):
        title1 = self.gettext(*self.radio_title1_loc)
        logger.info("投票选项1标题：%s" % title1)
        title2 = self.gettext(*self.radio_title2_loc)
        logger.info("投票选项2标题：%s" % title2)
        title3 = self.gettext(*self.radio_title3_loc)
        logger.info("投票选项3标题：%s" % title3)

    def showVoteTitle(self):
        mainTitle = self.gettext(*self.vote_title_loc)
        logger.info("投票标题：%s" % mainTitle)

