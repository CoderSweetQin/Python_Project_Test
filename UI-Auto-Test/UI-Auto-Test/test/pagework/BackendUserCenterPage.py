# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from test.pagework.BasePage import BasePage
from selenium.webdriver.support.select import Select

# 继承BasePage类
class BackendUCPage(BasePage):
    # select定位器
    select_menu = (By.XPATH, "/html/body/div[2]/div/div[1]/select")

    #切换到会员中心模块
    def UCInfo(self):
        Select(self.findElement(*self.select_menu)).select_by_value("fffe987d-db14-42e2-3331-5d4e386ec001")
        time.sleep(5)



