# coding = UTF-8

# Author: baiguoqiang
# Time : 2017/5/22 11:46

import pymysql.cursors
from config.env import DBConfig
from lib.mysql_ssh import MySQLExecutor


class DB:
    @staticmethod
    def __getconn(host, port, dbname, username, password):
        """获取数据库连接"""
        try:
            connection = pymysql.connect(host=host,
                                         port=int(port),
                                         db=dbname,
                                         user=username,
                                         password=password,
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            return connection
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    @staticmethod
    def get_dfb_conn():
        """获取账务系统连接"""
        return DB.__getconn(DBConfig.dfb_ult_host, DBConfig.dfb_ult_port, DBConfig.dfb_ult_db,
                            DBConfig.dfb_ult_user,
                            DBConfig.dfb_ult_password)

    @staticmethod
    def get_account_conn():
        """获取账务系统连接"""
        return DB.__getconn(DBConfig.account_ult_host, DBConfig.account_ult_port, DBConfig.account_ult_db,
                            DBConfig.account_ult_user,
                            DBConfig.account_ult_password)

    @staticmethod
    def get_uc_db_conn():
        """获取user center 数据库连接"""

        return DB.__getconn(DBConfig.uc_ult_host, DBConfig.uc_ult_port, DBConfig.uc_ult_db, DBConfig.uc_ult_user,
                            DBConfig.uc_ult_password)

    @staticmethod
    def get_credit_db_conn():
        """获取信用评估数据库连接"""

        return DB.__getconn(DBConfig.credit_ult_host, DBConfig.credit_ult_port, DBConfig.credit_ult_db,
                            DBConfig.credit_ult_user, DBConfig.credit_ult_password)

    @staticmethod
    def get_qyd_db_conn():
        """获取轻易贷数据库连接"""

        return DB.__getconn(DBConfig.qyd_ult_host, DBConfig.qyd_ult_port, DBConfig.qyd_ult_db,
                            DBConfig.qyd_ult_user, DBConfig.qyd_ult_password)

    # close database
    @staticmethod
    def close(self):
        self.connection.close()


class MySQLExecutorProvider(MySQLExecutor):
    """通过跳板机操作轻易分期数据库"""

    def get_credit_executor(self):
        """轻易分期授信库"""
        return self.get_instance(dbip=DBConfig.credit_host_ssh, dbusername=DBConfig.credit_user_ssh,
                                 dbpwd=DBConfig.credit_password_ssh, dbinstance=DBConfig.credit_instance_ssh)

    def get_uc_executor(self):
        """用户中心库"""
        return self.get_instance(dbip=DBConfig.uc_host_ssh, dbusername=DBConfig.uc_user_ssh,
                                 dbpwd=DBConfig.uc_password_ssh, dbinstance=DBConfig.uc_instance_ssh)

    def get_qyd_executor(self):
        """轻易贷库"""
        return self.get_instance(dbip=DBConfig.qyd_host_ssh, dbusername=DBConfig.qyd_user_ssh,
                                 dbpwd=DBConfig.qyd_password_ssh, dbinstance=DBConfig.qyd_instance_ssh)


if __name__ == "__main__":
    conn = DB.get_qyd_db_conn()
    qyd_db_cursor = conn.cursor()
    sql6 = "select id from user where tel_num='13236692451'"  # 查询轻易贷user_id
    qyd_db_cursor.execute(sql6)
    result = qyd_db_cursor.fetchall()
    print(result)
    qyd_userid = result[0]['id']