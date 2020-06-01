# coding = UTF-8

# Author: baiguoqiang
# Time : 2017/6/9 22:15
import paramiko as p
from config.env import DBConfig


class MySQLExecutor(object):
    """通过连跳板机执行mysql语句"""

    def get_instance(self, dbip, dbusername, dbpwd, dbinstance):
        self.dbip = dbip
        self.dbusername = dbusername
        self.dbpwd = dbpwd
        self.dbinstance = dbinstance
        return self

    def select(self, sql):
        """mysql执行select语句"""
        cmd = 'mysql -h ' + self.dbip + ' -u' + self.dbusername + ' -p' + self.dbpwd + ' ' + self.dbinstance + ' -e "' + sql + '"'
        collection = self.__command(DBConfig.db_proxy_host_ip, DBConfig.db_proxy_host_port,
                                    DBConfig.db_proxy_host_username, DBConfig.db_proxy_host_password, cmd)
        header = collection[0].decode('utf-8').strip('\n').split('\t')
        row_num = len(collection)  # 获取行数
        data_list = []
        for i in range(1, row_num):  # 读取行
            row_data = collection[i].decode('utf-8').strip('\n').split('\t')  # 读取行中的每一列的值
            d = dict(zip(header, row_data))
            data_list.append(d)
        return data_list

    def update(self, sql):
        """mysql执行update语句"""
        cmd = 'mysql -h ' + self.dbip + ' -u' + self.dbusername + ' -p' + self.dbpwd + ' ' + self.dbinstance + ' -e "' + sql + '"'
        self.__command(DBConfig.db_proxy_host_ip, DBConfig.db_proxy_host_port,
                       DBConfig.db_proxy_host_username, DBConfig.db_proxy_host_password, cmd)

    def __command(self, host, port, username, password, cmd):  # 定义执行命令方法cmd为执行命令参数
        client = p.SSHClient()  # 建立远程连接SSH
        client.load_system_host_keys()
        client.set_missing_host_key_policy(p.AutoAddPolicy())  # 自动设置权限
        print('*** Connecting...')
        client.connect(host, port, username, password)  # 连接远程服务器
        print('*** Here we go!\n')
        session = client._transport.open_session()  # 建立一个会话
        session.exec_command(cmd)  # 执行命令
        stdout = session.makefile('rb')  # 建立读文件流
        result = stdout.readlines()  # 输出所有执行命令后的信息list型
        return result


if __name__ == "__main__":
    sql0 = "select * from OTP order by createTime desc limit 5;"
    xx = MySQLExecutor().select("172.60.0.199", "platform", "platform", "che001", sql0)