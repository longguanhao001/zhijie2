from appium import webdriver
from appium.webdriver.webdriver import WebDriver

class ClientDriver(object):
    driver : WebDriver
    # 后期从jenkins获取的参数
    device = "ios"
    env = "test"
    channel = "pure"

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

            cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            cls.driver.implicitly_wait(10)
            return cls.driver