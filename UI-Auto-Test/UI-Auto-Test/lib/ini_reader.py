# coding = UTF-8

# Author: baiguoqiang
# Time : 2017/5/22 11:46

import configparser


class INIReader:
    """
    专门读取配置文件的，.ini文件格式
    """

    def __init__(self, filename):
        configpath = filename
        fd = open(configpath, encoding="UTF-8")
        data = fd.read()
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath, encoding="UTF-8")

    def getValue(self, env, name):
        """
        [projectConfig]
        project_path=E:/Python-ProjectConfig/UItestframework
        :param env:[projectConfig]
        :param name:project_path
        :return:E:/Python-ProjectConfig/UItestframework
        """
        return self.cf.get(env, name)
