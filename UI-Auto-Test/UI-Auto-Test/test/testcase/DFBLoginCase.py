# -*- coding: utf-8 -*-
import unittest
from test.pagework.OpenPage import OpenPage
from test.testcase.BasetestCase import BasetestCase
from test.pagework.BackendUserCenterPage import BackendUCPage
from tools.log import logger
# from lib.mysql_db import DB

class DFBLoginCase(BasetestCase,OpenPage):

    def test_login001(self):
        logger.info(u"open the booking agent!!!")
        self.open()
        # logger.info(u"打开垫付宝管理台会员中心模块")
        # self.UCInfo()
        # conn=DB.get_dfb_conn()



if __name__=="__main__":
    unittest.main(verbosity=2)
