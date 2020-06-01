# coding=utf-8
import unittest
import os
from HTMLTestRunner001 import HTMLTestRunner
from tools.sendmail import SendMail
import codecs
from lxml import etree
from tools.log import logger
from config.configDict import config
import time

# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './test/testcase'
test_dir_abs = os.path.abspath(test_dir)
discover = unittest.defaultTestLoader.discover(test_dir_abs, pattern='*.py')

def getText(content):
    rc = []
    for node in content.itertext():
        rc.append(node.strip())
    return ''.join(rc)

def printcasesummary(filename):
    f = codecs.open(filename, "r", "utf-8")
    content = f.readlines()
    f.close()
    tree = etree.HTML(str(content))
    nodeCaseStartTime = tree.xpath(u"//div[@class='heading']/p[1]")[0]
    nodeCaseDuration = tree.xpath(u"//div[@class='heading']/p[2]")[0]
    nodeCaseNum = tree.xpath(u"//div[@class='heading']/p[3]")[0]
    logger.info("**************************用例执行概况*****************************\n")
    logger.info(getText(nodeCaseStartTime) + "\n")
    logger.info(getText(nodeCaseDuration) + "\n")
    logger.info(getText(nodeCaseNum) + "\n")

def FireFox_Test():
    config['Browse_Type'] = 2 # 1=FireFox  2=Chrome 3=IE
    config['dfburl'] = "https://integcert.synxis.com/xbe/rez.aspx?Hotel=20116&Chain=7666"
    content = "config=" + str(config)
    print(content)
    with open("config/configDict.py", 'w')as f:
        f.write(content)
    proj_path = os.path.dirname(os.path.dirname(__file__))
    print(proj_path)
    reportPath = proj_path + "/auto-ui/report"
    logger.info(reportPath)
    filename = reportPath + '/FireFox_Test_Result'+time.strftime("%Y-%m-%d--%H_%M_%S")+'.html'  # jenkins中的html report插件可以关联到每个build
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, verbosity=1, title='接口自动化测试报告', description='测试执行总结')
    runner.run(discover)
    fp.close()
    sendMail = SendMail()
    sendMail.send()
    # printlog2console()
    printcasesummary(filename=filename)
    logger.info("详情请查询 HTML Report")
    time.sleep(3)

if __name__ == "__main__":
    FireFox_Test()

