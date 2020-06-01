#coding:utf-8

import unittest
from config.configDict import config
from test.comwork import OpenBrower
from tools.log import logger

class BasetestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        logger.info('############################### NEW CASE START ###############################')
        self.brotype = config['Browse_Type']
        self.url = config['dfburl']
        self.driver = OpenBrower.is_brower(self.brotype, self.url)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        logger.info('###############################  END  ###############################')
