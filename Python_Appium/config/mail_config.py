import os
import logging

"""邮件配置"""
sender = 'test@test.net'
receiver = 'xiaoli@test.net'
"""登陆邮箱的用户名"""
emailusername = 'test@test.net'
"""登陆邮箱的授权码"""
emailpassword = 'lqke001@#'
"""smtp服务器"""
server = 'mail.test.net'
"""数据目录"""
datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

"""项目配置"""
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""日志配置"""

logpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log')
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%y-%m-%d %H:%M',
                    filename=os.path.join(logpath, 'log.txt'),
                    filemode='a')
