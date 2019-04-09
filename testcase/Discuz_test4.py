from testcase.basetestcase import BaseTestCase
from pageobjects.login_page import loginPage
from pageobjects.moren_page import SendTiePage
from pageobjects.vote_page import VotePage
from framework.logger import Logger
import time

logger=Logger(logger="Flow4").getlog()
class Flow4(BaseTestCase):

    def test_flow4(self):
        """
        Discuz业务流程四
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
        #2.发表投票帖子
        send_page = SendTiePage(self.driver)
        #点击默认板块
        send_page.click_moren()
        vote_page = VotePage(self.driver)
        vote_page.click_SendTie_btn()
        vote_page.click_StartVote_btn()
        vote_page.voteInfo("选班长", "小明", "小红", "小白", "谁的票多谁是班长！")
        vote_page.vote()

        #3.取出投票各个选项的名称以及投票比例
        vote_page.showVoteName()
        vote_page.showVotePer()

        #4.取出投票标题
        vote_page.showVoteTitle()















        # home_page = HomePage(self.driver)
        # base_page=BasePage(self.driver)
        # home_page.login("admin", "lyf2580")
        # home_page.moren_click()
        # #判断是否进入默认板块
        # moren_part_text=base_page.gettext(*home_page.moren_text_loc)
        # self.assertEqual(moren_part_text,"默认版块",msg="进入默认板块失败")
        # home_page.vote_fatie("投票标题","001","002","003","投票文本内容")
        #
