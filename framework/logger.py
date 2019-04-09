import logging
import time
import os
#创建一个logging对象
class Logger(object):
    def __init__(self,logger):
        """
        指定保存日志文件的路径，日志级别，以及调用文件
        将日志存入到指定文件中
        :param logger:
        """

        #创建一个logger
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler，写入日志中(日志输出至哪里)
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        #项目根目录下的/Logs保存日志
        log_path=os.path.dirname(os.path.abspath('.'))+'/Discuz_autoTestFrame/logs/'
        log_name=log_path+rq+'.log'

        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #设置handler的日志格式
        formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getlog(self):
        return self.logger

