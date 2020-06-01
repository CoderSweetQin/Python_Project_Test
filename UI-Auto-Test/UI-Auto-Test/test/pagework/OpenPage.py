# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from test.pagework.BasePage import BasePage
from selenium.webdriver.support.select import Select
from tools.log import logger
import time

# 继承BasePage类
class OpenPage(BasePage):
    # button定位器
    detail = (By.NAME, "V150$C1$CBtn")

    # 打开一个hrefV151_C1_AR_ctl07_RateRoomSectionHeaderCntrl_ToggleTextDiv
    href=(By.ID,"V151_C1_AR_ctl12_RateRoomSectionHeaderCntrl_ToggleTextDiv")

    # href=(By.ID,"V151_C1_AR_ctl07_RateRoomSectionHeaderCntrl_ToggleTextDiv")

    # 选择一个hotel
    hotel=(By.ID,"V151_C1_AR_ctl12_AVP_ctl12_SPB")

    # 选择一个packageid
    packageid=(By.ID,"V159_C0_SelectPackagesButton")

    call_name=(By.ID,"V152_C0_gi_TitleDropDownList")
    # call_name1=(By.XPATH,"//*[@id=\"V152_C0_gi_TitleDropDownList\"]/option[2]")

    name2=(By.ID,"V152_C0_gi_FirstNameTextBox")
    xing2=(By.ID,"V152_C0_gi_LastNameTextBox")

    email=(By.ID,"V152_C0_gi_EmailTextBox")
    confirm_email=(By.ID,"V152_C0_gi_RetypeEmailTextBox")


    address=(By.ID,"V152_C0_ga_Address1TextBox")
    city=(By.ID,"V152_C0_ga_CityTextBox")

    provence=(By.ID,"V152_C0_ga_StateDropDownList")
    choice=(By.XPATH,"//*[@id=\"V152_C0_ga_StateDropDownList\"]/option[4]")

    phone=(By.ID,"V152_C0_ga_DaytimePhoneTextBox")
    payment_type=(By.ID,"V152_C0_cc_PaymentTypeDropDownList")
    payment_type_1=(By.XPATH,"//*[@id=\"V152_C0_cc_PaymentTypeDropDownList\"]/option[2]")

    card_name=(By.ID,"V152_C0_cc_CardHolderNameTextBox")
    card_number=(By.ID,"V152_C0_cc_CardNumberTextBox")

    enddate=(By.ID,"V152_C0_cc_ExpirationMonthDropDownList")
    enddate1=(By.ID,"V152_C0_cc_ExpirationYearDropDownList")

    yes=(By.XPATH,"//*[@id=\"V152_C0_OptInCntrl_OptInTable\"]/span/label")
    yes1=(By.XPATH,"//*[@id=\"V152_C0_pa_PrivacyPolicyAckCheckPanel\"]/span[2]/label")
    yes2=(By.ID,"V152_C0_pa_PolicyAckLabel")

    confirm_button=(By.ID,"V152_C0_ConfirmButton")

    def open(self):
        try:
            print("click a button!!!")
            self.findElement(*self.detail).click()
            time.sleep(3)
            print("click a herf!!!")
            self.findElement(*self.href).click()
            time.sleep(5)
            logger.info("chooice a hotel!!!")
            self.findElement(*self.hotel).click()
            time.sleep(8)
            logger.info("chooice a package!!!")
            self.findElement(*self.packageid).click()
            time.sleep(5)
            Select(self.findElement(*self.call_name)).select_by_value("Mr.")

            self.findElement(*self.name2).send_keys("wu")
            self.findElement(*self.xing2).send_keys("Tony")
            time.sleep(5)

            self.findElement(*self.email).send_keys("loadkernel@126.com")
            self.findElement(*self.confirm_email).send_keys("loadkernel@126.com")
            self.findElement(*self.address).send_keys("test address")
            self.findElement(*self.city).send_keys("bj")
            time.sleep(2)
            # Select(self.findElement(*self.provence)).select_by_value("北京")
            self.findElement(*self.provence).click()
            self.findElement(*self.choice).click()

            self.findElement(*self.phone).send_keys("13120323258")
            time.sleep(2)
            self.findElement(*self.payment_type).click()
            self.findElement(*self.payment_type_1).click()
            time.sleep(5)

            self.findElement(*self.card_name).send_keys("tony")
            self.findElement(*self.card_number).send_keys("378282246310005")
            Select(self.findElement(*self.enddate)).select_by_value("12")
            Select(self.findElement(*self.enddate1)).select_by_value("2019")


            self.findElement(*self.yes).click()
            self.findElement(*self.yes1).click()
            self.findElement(*self.yes2).click()

            self.findElement(*self.confirm_button).click()
            time.sleep(5)


        except Exception as msg:
            logger.info("openPage 打开异常原因:%s"%msg)




        


