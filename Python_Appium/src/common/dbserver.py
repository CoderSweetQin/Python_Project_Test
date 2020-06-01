import pymysql.cursors
import pymysql
from config import db_configs
import importlib, sys
importlib.reload(sys)


class mysqldb(object):
    """数据库连接信息"""
    def __init__(self, dbName):
        if dbName == "front":
            self.conn = db_configs.front
        elif dbName == "testnewdb":
            self.conn = db_configs.testnewdb
        elif dbName == "testdb":
            self.conn = db_configs.testdb
        elif dbName == "testaccount":
            self.conn = db_configs.testaccount
        elif dbName == "account":
            self.conn = db_configs.account
        elif dbName == "ucenter":
            self.conn = db_configs.ucenter
        elif dbName == "transaction":
            self.conn = db_configs.transaction
        elif dbName == "Azure_qa_testdata":
            self.conn = db_configs.Azure_qa_testdata
        else:
            pass

    def selectsql(self, sql):
        con = pymysql.connect(**self.conn)
        cursor = con.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        con.close()
        return data

    def updatesql(self, sql):
        conn = pymysql.connect(**self.conn)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
