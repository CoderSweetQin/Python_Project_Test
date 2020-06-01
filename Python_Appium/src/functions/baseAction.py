from selenium.webdriver.support.ui import WebDriverWait


class BaseAction(object):
    """对元素操作的公共方法进行封装，并增加日志记录处理"""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, ele_type, value):
        """
        查询页面元素，增加显性时间等待机制
        :param ele_type: 元素定位方式
        :param value: 元素定位属性值
        :return: ele(WebElement)：返回查找到的元素对象
        """
        ele = None
        try:
            if ele_type == "id":
                WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id(value))
                ele = self.driver.find_element_by_id(value)
            elif ele_type == "name":
                WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_name(value))
                ele = self.driver.find_element_by_name(value)
            elif ele_type == "link_text":
                WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_link_text(value))
                ele = self.driver.find_element_by_link_text(value)
            elif ele_type == "partial_link_text":
                WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_partial_link_text(value))
                ele = self.driver.find_element_by_partial_link_text(value)
            elif ele_type == "tag_name":
                WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_tag_name(value))
                ele = self.driver.find_element_by_tag_name(value)
            elif ele_type == "xpath":
                WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_xpath(value))
                ele = self.driver.find_element_by_xpath(value)
            elif ele_type == "class_name":
                WebDriverWait(self.driver, 1).until(lambda driver: driver.find_element_by_class_name(value))
                ele = self.driver.find_element_by_class_name(value)
            else:
                print("没有这种元素定位方式{}".format(ele_type))
        except Exception as e:
            print(e)
        else:
            return ele
