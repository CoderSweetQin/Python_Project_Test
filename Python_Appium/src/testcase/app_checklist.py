import unittest
import os, time
import requests
from config import url
from src.common.iniHelper import *
from src.common.appium_start import appium_start
from src.common.test_sql import test_app_login
from src.functions.baseAction import BaseAction
from src.common.log import logger as log
from src.common.qy_open_loan import qy_amount_open
from decimal import *


class CheckList(unittest.TestCase):
    def setUp(self):
        """初始化app driver"""
        self.driver = appium_start()

    def test_001_login(self):
        """APP登录测试"""
        time.sleep(8)
        # ele_earn_money = iniHelper("login", "earn_money")
        # ele_update_version_icon = iniHelper("login", "update_version")
        # ele_close_update_version = iniHelper("login", "close_update_version")
        """1、引导页面：点击[赚钱]"""
        # BaseAction(self.driver).find_element("id", ele_earn_money).click()
        """2、关闭新版本推送通知"""
        # update_icon = BaseAction(self.driver).find_element("id", ele_update_version_icon)
        # if update_icon is not None:
        #     self.driver.tap([(843, 606)])
        #     BaseAction(self.driver).find_element("class_name", ele_close_update_version).click()
        #     time.sleep(3)
        # else:
        #     log.info("no push new version update !!!")

        """3、点击右下角图标：账户"""
        self.driver.tap([(912, 1855)])
        ele_account = iniHelper("login", "account_text")
        BaseAction(self.driver).find_element("class_name", ele_account).click()
        """4、进入登录页面，使用用户名和密码登录"""
        ele_login_phone = iniHelper("login", "username")
        ele_login_pwd = iniHelper("login", "password")
        ele_login_submit = iniHelper("login", "login_submit")
        data_login_phone = iniHelper("input_testdata", "login_phone")
        data_login_pwd = iniHelper("input_testdata", "login_pwd")
        BaseAction(self.driver).find_element("id", ele_login_phone).click()
        BaseAction(self.driver).find_element("id", ele_login_phone).clear()
        BaseAction(self.driver).find_element("id", ele_login_phone).send_keys(data_login_phone)
        BaseAction(self.driver).find_element("id", ele_login_pwd).click()
        BaseAction(self.driver).find_element("id", ele_login_pwd).clear()
        BaseAction(self.driver).find_element("id", ele_login_pwd).send_keys(data_login_pwd)
        BaseAction(self.driver).find_element("id", ele_login_submit).click()
        time.sleep(5)
        """5、登录完成，查看是否登录成功"""
        ele_account = iniHelper("login", "account_icon")
        BaseAction(self.driver).find_element("id", ele_account).click()
        is_login_account = iniHelper("login", "is_login_icon")
        if is_login_account is not None:
            log.info("login is success !!!")
        else:
            log.info("login is failed !!!")

    # def test_002_invest(self):
        """6、购买青盈"""
        ele_invest_icon = iniHelper("invest_product", "invest_icon")
        BaseAction(self.driver).find_element("id", ele_invest_icon).click()
        headers = {
            "X-Auth-Token": test_app_login(iniHelper("input_testdata", "login_phone"),
                                          iniHelper("input_testdata", "login_pwd"))
        }
        amount_result = requests.post(url=url.query_qy_amount, headers=headers, verify=False).json()

        """6.1、查询青盈剩余可投金额,金额大于200,则立即购买青盈,否则调用青盈开标接口进行开标成功后再购买"""
        if Decimal(amount_result["data"]["xqy"]["data"]["totalAmount"]).quantize(Decimal("0.00")) >= \
                Decimal(200.00).quantize(Decimal("0.00")):
            ele_qy_investpage = iniHelper("invest_product", "investpage_qy_ele")
            ele_qyinfo_buy = iniHelper("invest_product", "qyinfo_buy_ele")
            ele_confirm_buy_qy = iniHelper("invest_product", "confirm_buy_qy")
            BaseAction(self.driver).find_element("id", ele_qy_investpage).click()
            BaseAction(self.driver).find_element("id", ele_qyinfo_buy).click()
            BaseAction(self.driver).find_element("class_name", ele_confirm_buy_qy).send_keys(iniHelper("input_testdata",
                                                                                                       "buy_qy_amount"))
            os.popen("adb shell input tap " + str(644.0) + " " + str(1263.0))
            ele_return_account = iniHelper("invest_product", "return_account")
            BaseAction(self.driver).find_element("class_name", ele_return_account).click()
            self.driver.tap([(231, 1103)])
            BaseAction(self.driver).find_element("class_name", ele_return_account).click()
            log.info("auto_buy qy success!!!")
            log.info("auto_qya success and return account page success!!!")
        else:
            """6.2、青盈剩余可投小于200调用青盈开标接口"""
            ele_qy_open_phone = iniHelper("open_qy_loan", "phone")
            ele_qy_open_amount = iniHelper("open_qy_loan", "amount")
            open_result = qy_amount_open(ele_qy_open_phone, ele_qy_open_amount)
            time.sleep(5)
            if str(open_result) == 'SUCCESS':
                log.info("That is a new qy_loan created successfully!!!")
                ele_qy_investpage = iniHelper("invest_product", "investpage_qy_ele")
                ele_qyinfo_buy = iniHelper("invest_product", "qyinfo_buy_ele")
                ele_confirm_buy_qy = iniHelper("invest_product", "confirm_buy_qy")
                BaseAction(self.driver).find_element("id", ele_qy_investpage).click()
                BaseAction(self.driver).find_element("id", ele_qyinfo_buy).click()
                BaseAction(self.driver).find_element("class_name", ele_confirm_buy_qy).send_keys(iniHelper(
                    "input_testdata", "buy_qy_amount"))
                os.popen("adb shell input tap " + str(644.0) + " " + str(1263.0))
                self.driver.find_element_by_class_name("android.view.View").click()
                ele_return_account = iniHelper("invest_product", "return_account")
                BaseAction(self.driver).find_element("class_name", ele_return_account).click()
                self.driver.tap([(231, 1103)])
                BaseAction(self.driver).find_element("class_name", ele_return_account).click()
                log.info("auto_buy qy success!!!")
                log.info("auto_qya success and return account page success!!!")
            else:
                log.info("That is a new qy_loan created failed!!!")

    # def test_003_recharge(self):
    #     """7、快捷充值"""
    #     self.driver.tap([(813, 1102)])
    #     ele_recharge_text = iniHelper("recharge", "recharge_step1")
    #     ele_recharge_bank = iniHelper("recharge", "recharge_step2")
    #     ele_recharge_amount = iniHelper("recharge", "recharge_step3")
    #     ele_recharge_submit = iniHelper("recharge", "recharge_step4")
    #     BaseAction(self.driver).find_element("class_name", ele_recharge_text).click()
    #     time.sleep(2)
    #     BaseAction(self.driver).find_element("id", ele_recharge_bank).click()
    #     BaseAction(self.driver).find_element("id", ele_recharge_amount).send_keys(iniHelper("input_testdata",
    #                                                                                         "recharge_amount"))
    #     BaseAction(self.driver).find_element("id", ele_recharge_submit).click()
    #     time.sleep(15)
    #     self.driver.tap([(354, 711)])
    #     ele_recharge_password = iniHelper("recharge", "recharge_pwd")
    #     BaseAction(self.driver).find_element("class_name", ele_recharge_password).send_keys(iniHelper("input_testdata",
    #                                                                                                   "transaction_pwd"))
    #     self.driver.tap([(54, 969)])
    #     ele_recharge_button = iniHelper("recharge", "recharge_sumit")
    #     BaseAction(self.driver).find_element("class_name", ele_recharge_button).click()
    #     self.driver.tap([(509, 1027)])
    #     ele_return_account = iniHelper("recharge", "return_account")
    #     BaseAction(self.driver).find_element("class_name", ele_return_account).click()
    #     log.info("recharge success and return account page success !!!")

    # def test_004_withdraw(self):
    #     """8、提现"""
    #     self.driver.tap([(546, 1102)])
    #     ele_withdraw_text = iniHelper("withdraw", "withdraw_step1")
    #     ele_withdraw_money = iniHelper("withdraw", "withdraw_step2")
    #     ele_withdraw_submit = iniHelper("withdraw", "withdraw_step3")
    #     BaseAction(self.driver).find_element("class_name", ele_withdraw_text).click()
    #     BaseAction(self.driver).find_element("id", ele_withdraw_money).send_keys(iniHelper("input_testdata",
    #                                                                                        "withdraw_amount"))
    #     BaseAction(self.driver).find_element("id", ele_withdraw_submit).click()
    #     time.sleep(2)
    #     self.driver.tap([(354, 627)])
    #     ele_withdraw_pwd = iniHelper("withdraw", "withdraw_pwd")
    #     ele_withdraw_button = iniHelper("withdraw", "withdraw_submit")
    #     BaseAction(self.driver).find_element("class_name", ele_withdraw_pwd).send_keys(iniHelper("input_testdata",
    #                                                                                              "transaction_pwd"))
    #     self.driver.tap([(54, 885)])
    #     BaseAction(self.driver).find_element("class_name", ele_withdraw_button).click()
    #     time.sleep(2)
    #     self.driver.tap([(54, 1551)])
    #     ele_withdraw_return_account = iniHelper("withdraw", "return_account")
    #     BaseAction(self.driver).find_element("class_name", ele_withdraw_return_account).click()
    #     log.info("withdraw success and return account page success!!!")
    #
    # def test_005_transfer(self):
    #     """9、青盈转让"""
    #     ele_qy_possession = iniHelper("product_transfer", "qy_possession")
    #     BaseAction(self.driver).find_element("id", ele_qy_possession).click()
    #     time.sleep(2)
    #     self.driver.tap([(740, 1827)])
    #     ele_qy_transfer_text = iniHelper("product_transfer", "qy_transfer_text")
    #     BaseAction(self.driver).find_element("class_name", ele_qy_transfer_text).click()
    #     time.sleep(7)
    #     self.driver.tap([(115, 521)])
    #     ele_qy_transfer_amount = iniHelper("product_transfer", "qy_transfer_amount")
    #     BaseAction(self.driver).find_element("class_name", ele_qy_transfer_amount).send_keys(iniHelper(
    #         "input_testdata", "transfer_qy_amount"))
    #     self.driver.tap([(466, 1039)])
    #     BaseAction(self.driver).find_element("class_name", ele_qy_transfer_text).click()
    #     self.driver.tap([(442, 932)])
    #     BaseAction(self.driver).find_element("class_name", ele_qy_transfer_text).click()
    #     self.driver.tap([(231, 939)])
    #     ele_return_account = iniHelper("product_transfer", "return_account")
    #     BaseAction(self.driver).find_element("class_name", ele_return_account).click()
    #     log.info("qy_transfer success and return account page success!!!")
    #
    # def test_006_logout(self):
    #     """10、退出登录"""
    #     ele_logout_icon = iniHelper("logout", "real_name")
    #     BaseAction(self.driver).find_element("id", ele_logout_icon).click()
    #     time.sleep(3)
    #     x = self.driver.get_window_size()['width']
    #     y = self.driver.get_window_size()['height']
    #     self.driver.swipe(x / 2, y * 0.8, x / 2, y * 0.2, 200)
    #     time.sleep(3)
    #     os.popen("adb shell input tap " + str(659.0) + " " + str(1834.0))
    #     ele_logout_text = iniHelper("logout", "logout_text")
    #     BaseAction(self.driver).find_element("class_name", ele_logout_text).click()
    #     os.popen("adb shell input tap " + str(945.0) + " " + str(1140.0))
    #     ele_logout_confirm = iniHelper("logout", "confirm_logout")
    #     BaseAction(self.driver).find_element("id", ele_logout_confirm).click()
    #     log.info("logout success!!!")
    #
    # def tearDown(self):
    #     self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=1)