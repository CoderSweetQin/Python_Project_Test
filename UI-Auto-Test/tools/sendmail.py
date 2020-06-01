# coding:utf-8

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tools.log import Log
import configparser as cparser

proj_path = os.path.dirname(os.path.dirname(__file__))

# 测试报告的路径
reportPath = proj_path + "/report"
logger = Log()

# ======== Reading email_config.ini setting, init vars===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/config/email_config.ini"
cf = cparser.ConfigParser()
cf.read(file_path, encoding="UTF-8")
mail_user = cf.get("emails", "mail_user")
mail_pwd = cf.get("emails", "mail_pwd")
mail_to = cf.get("emails", "mail_to")
subject = cf.get("emails", "subject")
mail_host = cf.get("emails", "mail_host")


class SendMail:
    def __init__(self, receiver=None):
        """接收邮件的人：list or tuple"""
        if receiver is None:
            self.sendTo = mail_to
        else:
            self.sendTo = receiver

    def __get_report(self):
        """获取最新测试报告"""
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname

    def __take_messages(self):
        """生成邮件的内容，和html报告附件"""
        newreport = self.__get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = '测试报告主题'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['from'] = mail_user
        try:
            smtp = smtplib.SMTP_SSL(mail_host, 465)
            smtp.login(mail_user, mail_pwd)
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
            smtp.close()
            logger.info("发送邮件成功")
        except Exception:
            logger.error('发送邮件失败')
            raise


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
