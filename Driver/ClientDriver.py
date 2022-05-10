import os
import time

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

class ClientDriver(object):
    driver: WebDriver
    # 后期从jenkins获取的参数
    device = "ios"
    env = "test"
    channel = "pure"

    @classmethod
    def deal_guideAndPop(cls, driver: WebDriver):
        # 处理导航页和更新弹窗
        try:
            driver.find_element(by="id", value="Next").click()
            driver.find_element(by="id", value="Next").click()
            driver.find_element(by="id", value="S T A R T").click()
        except:
            pass
        try:
            driver.find_element(by="id", value="icon x white delete").click()
        except:
            pass

    @classmethod
    def installApp(cls):
        # 安装app
        result = os.popen("ideviceinstaller -l").read()
        # 获取安装包文件
        file_name_list = os.listdir("../Package")

        if "video.test.tools.os" not in result:
            os.popen("ideviceinstaller -i '../Package/%s'" % file_name_list[0]).read()
        else:
            # 先卸载再删除
            os.popen("ideviceinstaller -U 'video.test.tools.os'").read()
            os.popen("ideviceinstaller -i '../Package/%s'" % file_name_list[0]).read()

    @classmethod
    def restartApp(cls):
        # 重启app
        if cls.device == "ios":
            caps = {}
            caps["platformName"] = "ios"
            caps["platformVersion"] = "14.6"
            caps["deviceName"] = "iPhone(2)"
            caps["app"] = "video.test.tools.os"
            caps["udid"] = "20a7adaffd52ebb0f01efea599592e4272297911"
            caps['xcodeOrgId'] = '3L4QK9YSAV'
            caps['xcodeSigningId'] = "iPhone Developer"
            caps['autoAcceptAlerts'] = True

            cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            cls.driver.implicitly_wait(10)
            if "Next" or "icon x" in str(cls.driver.page_source):
                cls.deal_guideAndPop(cls.driver)
            return cls.driver


