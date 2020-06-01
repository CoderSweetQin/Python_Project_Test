#  -*- coding: utf-8 -*-
__author__ = 'tony'

from selenium import webdriver
import time
from tools.log import logger

def is_brower(Browse_Type,url):
    if Browse_Type==1:
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        driver.get(url)
        logger.info("打开了火狐浏览器")
        driver.maximize_window()
        return driver
    elif Browse_Type==2:
        driver = webdriver.Chrome(executable_path="D:\\BaiduNetdiskDownload\\All\\All\\AllInHere\\auto-ui\lib\\chromedriver.exe")
        # self.driver.implicitly_wait(30)
        # self.driver.maximize_window()
        # driver =webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.get(url)
        logger.info("打开了谷歌浏览器")
        driver.maximize_window()
        time.sleep(2)
        return driver
    else:
        driver = webdriver.Ie("C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe")
        driver.implicitly_wait(30)
        driver.get(url)
        logger.info("打开了IE浏览器")
        driver.maximize_window()
        return driver

if __name__=='__main__':
  #函数调用
  is_brower(2,"www.baidu.com")