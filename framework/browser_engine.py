import os.path
from selenium import webdriver
from configparser import ConfigParser
from framework.logger import Logger

logger=Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath('.'))#相对路径获取方法
    print(dir)
    chromedriver_path=dir+"/Discuz_autoTestFrame/tools/chromedriver.exe"
    geckodriver_path = dir + "/Discuz_autoTestFrame/tools/geckodriver.exe"
    IEdriver_path = dir + "/Discuz_autoTestFrame/tools/IEDriverServer.exe"

    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/Discuz_autoTestFrame/config/config.ini'
        config.read(file_path)

        browser=config.get("browserType","browserName")
        logger.info("您已经选择了%s浏览器"%browser)
        url=config.get("testServer","URL")
        logger.info("The test Server is:%s "%url)

        if browser=="FireFox":
            driver = webdriver.Firefox(executable_path=self.geckodriver_path)
            logger.info("Starting firefox browser.")
        elif browser=="Chrome":
            driver=webdriver.Chrome(self.chromedriver_path)
            logger.info("Starting chrome browser.")
        elif browser=="IE":
            driver = webdriver.Ie(self.IEdriver_path)
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url:%s"%url)
        # 激活当前页面
        main_window = driver.current_window_handle
        driver.switch_to.window(main_window)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        self.dirver.quit()



