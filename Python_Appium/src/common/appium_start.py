import os
from src.common.iniHelper import *
from appium import webdriver


def appium_start():
    PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
    desired_cups = ini_sections("desired_cups")
    desired_cups['app'] = PATH(iniHelper("desired_cups", "app"))
    base_url = iniHelper("appium", "base_url")
    # print(base_url)
    # print(desired_cups)
    driver = webdriver.Remote(base_url, desired_cups)
    return driver
# appium_start()