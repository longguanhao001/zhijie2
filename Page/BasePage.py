import os
import time

import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Driver.ClientDriver import ClientDriver
import yaml

class BasePage():
    driver = None
    back_list = [("id", "Retry")]
    path = os.path.dirname(os.getcwd())
    error_times = 0

    def __init__(self):
        self.driver = self.getDriver()
    
    @classmethod
    def getDriver(cls):
        # 各个page获取diver的方法
        cls.driver = ClientDriver.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return ClientDriver

    def find(self, kv):
        #寻找元素的方法
        try:
            element = self.driver.find_element(*kv)
            self.error_times = 0
        except:
            # 如果没找到元素，则处理异常后重试
            for i in self.back_list:
                if i[1] in str(self.driver.page_source):
                    self.driver.find_element(by=i[0], value=i[1]).click()
            element = self.driver.find_element(*kv)
        return element

    def enter(self):
        # 输入后点击确定键
        windows = self.driver.get_window_size()
        target_height = int(int(windows["height"])*0.95)
        target_width = int(int(windows["width"])*0.9)
        self.driver.tap([(target_width, target_height)])

    def loadSteps(self, path: str, key, **kwargs):
        # 根据yaml文件解析测试用例
        path = path.replace("$channel", self.getClient().channel)
        file = open(path, "r")
        yaml_data = yaml.safe_load(file)
        steps = yaml_data[key]
        for step in steps:
            if "$" in step["locator"]:
                for k, v in kwargs.items(): # 参数化locator字段
                    step["locator"] = step["locator"].replace("$%s" % k, v)
            tuple_locator = (step["by"], step["locator"])
            action = str(step["action"]).lower()
            element = self.find(tuple_locator)
            if action == "click":
                element.click()
            elif action == "click&sleep":
                element.click()
                time.sleep(0.5)
            elif action == "findtext":
                return element.text
            elif action == "longclick":
                n = self.driver.get_clipboard_text()
                TouchAction(self.driver).long_press(element).perform()
            elif action == "sendkeys":
                text = str(step["text"])
                for k, v in kwargs.items(): # 参数化text段
                    text = text.replace("$%s" % k, v)
                element.set_value(text)
            elif action == "sendkeys&enter":
                text = str(step["text"])
                for k, v in kwargs.items():
                    text = text.replace("$%s" % k, v)
                element.set_value(text)
                self.enter()
            else:
                print("UNKONW KEYWORD")

    def swipe(self, keyword:str):
        # 滑动屏幕操作
        windows = self.driver.get_window_size()
        y = windows["height"]
        x = windows["width"]
        if keyword.lower() == "down":
            self.driver.swipe(1/2*x, 1/7*y, 1/2*x, 6/7*y, 200)
        elif keyword.lower() == "up":
            self.driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 7 * y, 200)
        elif keyword.lower() == "right":
            self.driver.swipe(1/7*x, 1/2*y, 5/7*x, 1/2*y, 200)
        elif keyword.lower() == "left":
            self.driver.swipe(6/7*x, 1/2*y, 1/7*x, 1/2*y, 100)
        time.sleep(2)

    def DeiverWaitExist(self,by,keyword):
        #显示等待toast存在
        toast_loc = ("%s" % by, "%s" % keyword)
        ele = WebDriverWait(self.driver, 10, 0.3).until(expected_conditions.visibility_of_element_located(toast_loc))
        return ele
    def DeiverWaitDisappear(self,by,keyword):
        #显示等待toast消失
        toast_loc = ("%s" % by, "%s" % keyword)
        ele = WebDriverWait(self.driver, 10, 0.3).until_not(expected_conditions.visibility_of_element_located(toast_loc))
        return ele


    def save_screenShot(self):
        # 保存截图到测试报告
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        deviceName = self.driver.caps["deviceName"]
        self.driver.get_screenshot_as_file(r"%s/ScreenShot/%s_%s.png" % (self.path, tm, deviceName))
        allure.attach.file(r"%s/ScreenShot/%s_%s.png" % (self.path, tm, deviceName), "运行截图", attachment_type=allure.attachment_type.PNG)

    def is_exits(self, located):
        try:
            tuple_locator = ("id", located)
            self.find(tuple_locator)
            return True
        except:
            return False