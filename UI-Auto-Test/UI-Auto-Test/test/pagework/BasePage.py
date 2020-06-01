# -*- coding: utf-8 -*-

from selenium.webdriver.support.expected_conditions import NoSuchElementException
from tools.log import logger
import time

class BasePage(object):
	def __init__(self,driver):
		self.driver=driver

	def findElement(self,*loc):
		try:
			return self.driver.find_element(*loc)
		except NoSuchElementException as e:
			nowTime = time.strftime("%Y%m%d.%H.%M.%S")
			self.driver.save_screenshot('test/screenshot/%s.jpg' % nowTime)
			logger.info('Error details :%s'%(e.args[0]))

	def findElements(self,*loc):
		try:
			return self.driver.find_elements(*loc)
		except NoSuchElementException as e:
			nowTime = time.strftime("%Y%m%d.%H.%M.%S")
			self.driver.save_screenshot('test/screenshot/%s.jpg' % nowTime)
			logger.info('Error details :%s'%(e.args[0]))

	def switch_to_Iframe(self,index):
		self.driver.switch_to.frame(index)














