import time

import allure

from Driver.ClientDriver import ClientDriver
import yaml

class BasePage():
    driver = None

    def __init__(self):
        self.driver = self.getDriver()
    
    @classmethod
    def getDriver(cls):
        cls.driver = ClientDriver.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return ClientDriver

    def find(self, kv):
        return self.driver.find_element(*kv)

    def enter(self):
        # 输入是点击确定键
        windows = self.driver.get_window_size()
        target_height = int(int(windows["height"])*0.95)
        target_width = int(int(windows["width"])*0.9)
        self.driver.tap([(target_width, target_height)])

    def loadSteps(self, path: str, key, **kwargs):
        path = path.replace("$channel", self.getClient().channel)
        file = open(path, "r")
        yaml_data = yaml.safe_load(file)
        steps = yaml_data[key]
        for step in steps:
            tuple_locator = (step["by"], step["locator"])
            element = self.find(tuple_locator)
            action = str(step["action"]).lower()
            if action == "click":
                element.click()
            elif action == "sendkeys":
                text = str(step["text"])
                for k, v in kwargs.items():
                    text = text.replace("$%s" % k, v)
                element.set_value(text)
            elif action == "sendkeys&enter":
                text = str(step["text"])
                for k, v in kwargs.items():
                    text = text.replace("$%s" % k, v)
                element.set_value(text)
                self.enter()
            elif action == "findtext":
                return element.text
            else:
                print("UNKONW KEYWORD")

    def save_screenShot(self):
        # 保存截图到测试报告
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        deviceName = self.driver.caps["deviceName"]
        self.driver.get_screenshot_as_file(r"../ScreenShot/%s_%s.png" % (tm, deviceName))
        allure.attach.file(r"../ScreenShot/%s_%s.png" % (tm, deviceName),"断言截图",attachment_type=allure.attachment_type.PNG)