"""读取ini配置文件工具类"""
from configparser import ConfigParser
import configparser
import importlib, sys
importlib.reload(sys)


class Myconf(configparser.ConfigParser):
    def __init__(self,defaults=None):
        configparser.ConfigParser.__init__(self, defaults=None)

    def optionxform(self, optionstr):
        return optionstr


def iniHelper(sections, option):
    cfg = Myconf()
    cfg.read('E:\\Appium_APP_auto\\config\\element.ini')
    cfg.sections()
    value = cfg.get(sections, option)
    print(value)
    return value
iniHelper("logout","logout_text")


def ini_sections(sections):
    cfg = Myconf()
    cfg.read('E:\\Appium_APP_auto\\config\\element.ini')
    cfg.sections()
    # value = cfg.options(sections)
    value = cfg.items(sections)
    value = dict(value)
    print(value)
    return value
ini_sections("desired_cups")