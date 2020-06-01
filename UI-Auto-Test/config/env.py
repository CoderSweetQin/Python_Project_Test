# coding = UTF-8

# Author: baiguoqiang
# Time : 2017/5/22 11:46
import os
import configparser
from lib.ini_reader import INIReader

# 项目根路径
project_path = os.path.dirname(os.path.dirname(__file__)).replace('\\', '/')


class ProjectConfig(object):
    """工程环境配置"""

    # 读取配置文件路径
    config_file = os.path.join(project_path, "config/config.ini")
    # 读取数据库配置文件
    db_config_file = os.path.join(project_path, "config/db.ini")
    # 日志路径
    log_path = os.path.join(project_path, 'log')
    # 测试报告路径
    report_path = os.path.join(project_path, 'report')
    # 测试数据路径
    test_data_path = os.path.join(project_path, 'testdata')
    # 测试用例路径
    test_case_path = os.path.join(project_path, 'case')


class DomainConfig(object):
    """测试环境配置"""
    # 读取配置文件内容
    cf = INIReader(ProjectConfig.config_file)
    env_type = cf.getValue("env", "env_type")
    if env_type == "stg":
        domain_qystg = cf.getValue("env", "domain_qystg_stg")
        domain_ppw = cf.getValue("env", "domain_ppw_stg")
        zk_ip = cf.getValue("env", "zk_ip_stg")
        zk_port = cf.getValue("env", "zk_port_stg")
    else:
        domain_qystg = cf.getValue("env", "domain_qystg_ult")
        domain_ppw = cf.getValue("env", "domain_ppw_ult")
        zk_ip = cf.getValue("env", "zk_ip_ult")
        zk_port = cf.getValue("env", "zk_port_ult")


class DBConfig(object):
    """数据库环境配置"""

    db_cf = INIReader(ProjectConfig.db_config_file)

    if DomainConfig.env_type == "stg":
        # 数据库跳板机ip
        db_proxy_host_ip = db_cf.getValue("dbenv", "host_stg")
        db_proxy_host_port = int(db_cf.getValue("dbenv", "port_stg"))
        db_proxy_host_username = db_cf.getValue("dbenv", "username_stg")
        db_proxy_host_password = db_cf.getValue("dbenv", "password_stg")

        # credit库
        credit_host_ssh = db_cf.getValue("qystag", "host_ult")
        credit_port_ssh = db_cf.getValue("qystag", "port_ult")
        credit_instance_ssh = db_cf.getValue("qystag", "db_name_ult")
        credit_user_ssh = db_cf.getValue("qystag", "user_ult")
        credit_password_ssh = db_cf.getValue("qystag", "password_ult")

        # 会员中心库
        uc_host_ssh = db_cf.getValue("uc", "host_ult")
        uc_port_ssh = db_cf.getValue("uc", "port_ult")
        uc_instance_ssh = db_cf.getValue("uc", "db_name_ult")
        uc_user_ssh = db_cf.getValue("uc", "user_ult")
        uc_password_ssh = db_cf.getValue("uc", "password_ult")

        # 轻易贷库
        qyd_host_ssh = db_cf.getValue("qyd_ult", "host_ult")
        qyd_port_ssh = db_cf.getValue("qyd_ult", "port_ult")
        qyd_instance_ssh = db_cf.getValue("qyd_ult", "db_name_ult")
        qyd_user_ssh = db_cf.getValue("qyd_ult", "user_ult")
        qyd_password_ssh = db_cf.getValue("qyd_ult", "password_ult")
    else:
        # 数据库跳板机ip,默认为ultimate
        db_proxy_host_ip = db_cf.getValue("dbenv", "host_ult")
        db_proxy_host_port = int(db_cf.getValue("dbenv", "port_ult"))
        db_proxy_host_username = db_cf.getValue("dbenv", "username_ult")
        db_proxy_host_password = db_cf.getValue("dbenv", "password_ult")

        # credit库
        credit_ult_host = db_cf.getValue("credit_ult", "host")
        credit_ult_port = db_cf.getValue("credit_ult", "port")
        credit_ult_db = db_cf.getValue("credit_ult", "db_name")
        credit_ult_user = db_cf.getValue("credit_ult", "user")
        credit_ult_password = db_cf.getValue("credit_ult", "password")

        credit_host_ssh = db_cf.getValue("qystag", "host_ult")
        credit_port_ssh = db_cf.getValue("qystag", "port_ult")
        credit_instance_ssh = db_cf.getValue("qystag", "db_name_ult")
        credit_user_ssh = db_cf.getValue("qystag", "user_ult")
        credit_password_ssh = db_cf.getValue("qystag", "password_ult")

        # 会员中心库
        uc_ult_host = db_cf.getValue("uc_ult", "host")
        uc_ult_port = db_cf.getValue("uc_ult", "port")
        uc_ult_db = db_cf.getValue("uc_ult", "db_name")
        uc_ult_user = db_cf.getValue("uc_ult", "user")
        uc_ult_password = db_cf.getValue("uc_ult", "password")

        uc_host_ssh = db_cf.getValue("uc", "host_ult")
        uc_port_ssh = db_cf.getValue("uc", "port_ult")
        uc_instance_ssh = db_cf.getValue("uc", "db_name_ult")
        uc_user_ssh = db_cf.getValue("uc", "user_ult")
        uc_password_ssh = db_cf.getValue("uc", "password_ult")

        # 轻易贷库
        qyd_ult_host = db_cf.getValue("qyd_ult", "host")
        qyd_ult_port = db_cf.getValue("qyd_ult", "port")
        qyd_ult_db = db_cf.getValue("qyd_ult", "db_name")
        qyd_ult_user = db_cf.getValue("qyd_ult", "user")
        qyd_ult_password = db_cf.getValue("qyd_ult", "password")

        qyd_host_ssh = db_cf.getValue("qyd", "host_ult")
        qyd_port_ssh = db_cf.getValue("qyd", "port_ult")
        qyd_instance_ssh = db_cf.getValue("qyd", "db_name_ult")
        qyd_user_ssh = db_cf.getValue("qyd", "user_ult")
        qyd_password_ssh = db_cf.getValue("qyd", "password_ult")

        # 账务系统库
        account_ult_host = db_cf.getValue("account_ult", "host")
        account_ult_port = db_cf.getValue("account_ult", "port")
        account_ult_db = db_cf.getValue("account_ult", "db_name")
        account_ult_user = db_cf.getValue("account_ult", "user")
        account_ult_password = db_cf.getValue("account_ult", "password")

        # 垫付宝前台库
        dfb_ult_host = db_cf.getValue("dfb_ult", "host")
        dfb_ult_port = db_cf.getValue("dfb_ult", "port")
        dfb_ult_db = db_cf.getValue("dfb_ult", "db_name")
        dfb_ult_user = db_cf.getValue("dfb_ult", "user")
        dfb_ult_password = db_cf.getValue("dfb_ult", "password")


class EMailConfig(object):
    """邮件配置"""
    file_path = project_path + "/config/config.ini"
    cf = configparser.ConfigParser()
    cf.read(file_path, encoding="UTF-8")
    sendemail = cf.get("email", "send_email")
    mail_user = cf.get("email", "mail_user")
    mail_pwd = cf.get("email", "mail_pwd")
    mail_to = cf.get("email", "mail_to")
    subject = cf.get("email", "subject")
    mail_host = cf.get("email", "mail_host")


if __name__ == "__main__":
    print(DomainConfig.domain_qystg)
