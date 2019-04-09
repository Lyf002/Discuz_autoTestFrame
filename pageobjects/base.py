from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import os
import time

logger=Logger(logger="BasePage").getlog()
class BasePage(object):

    def __init__(self,driver):
        self.driver=driver

    def get_screenshot(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/Discuz_autoTestFrame/screenshots/'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        rq=time.strftime(('%Y%m%d%H%M'),time.localtime(time.time()))
        screenshot_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screenshot_name)
            logger.info("截图成功")
        except Exception as e:
            self.get_screenshot()
            logger.error("截图失败！")

    def open_url(self,url):
        """打开浏览器"""
        self.driver.get(url)

    def get_webtitle(self):
        """获取页面title"""
        try:
            web_title=self.driver.title
            return web_title
        except Exception as e:
            self.get_screenshot()
            logger.error("当前页面title获取失败")

    def find_element(self,*loc):
        """定位页面元素"""
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info("%s找到页面元素%s"%(self,loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            self.get_screenshot()
            logger.error("%s页面元素未找到--%s"%(self,loc))


    def clear(self,*loc):
        """清除文本框内容"""
        element = self.find_element(*loc)
        try:
            element.clear()
            logger.info("清除搜索框内容")
        except Exception as e:
            self.get_screenshot()
            logger.error("清除内容失败！")

    def sendkeys(self,text,*loc):
        """在文本框中输入内容"""
        element=self.find_element(*loc)
        try:
            element.send_keys(text)
            logger.info("输入")
        except Exception as e:
            self.get_screenshot()
            logger.error("输入失败！")

    def click(self,*loc):
        """单击事件"""
        element = self.find_element(*loc)
        try:
            element.click()
            logger.info("点击")
        except Exception as e:
            self.get_screenshot()
            logger.error("单击失败！")

    def gettext(self,*loc):
        """获取元素相应的文本信息"""
        element=self.find_element(*loc)
        try:
            return element.text
            logger.info("%s获取%s" %(self,loc), "文本")
            print(element.text)
        except Exception as e:
            self.get_screenshot()
            logger.error("获取文本失败")

    def quit_browser(self):
        """退出浏览器"""
        self.driver.quit()

