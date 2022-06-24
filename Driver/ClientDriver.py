#  encoding: utf-8
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
        time.sleep(3)
        if "Next" in str(cls.driver.page_source):
            driver.find_element(by="id", value="Next").click()
            driver.find_element(by="id", value="Next").click()
            driver.find_element(by="id", value="S T A R T").click()
        time.sleep(3)
        if "icon x" in str(cls.driver.page_source):
            driver.find_element(by="id", value="icon x white delete").click()

    @classmethod
    def installApp(cls):
        # 安装app
        try:
            result = os.popen("/opt/homebrew/bin/ideviceinstaller -l").read()
            print(result)
            # 获取安装包文件
            path = os.path.dirname(os.getcwd())
            file_name_list = os.listdir("%s/Package" % path)
            cur_path = os.path.dirname(os.getcwd())
            package_path = "%s/Package/%s" % (cur_path, file_name_list[0])
            if "video.test.tools.os" not in result:
                os.popen("/opt/homebrew/bin/ideviceinstaller -u 20a7adaffd52ebb0f01efea599592e4272297911 -i '%s'" % package_path).read()
                os.remove(r"%s" % package_path)
            else:
                # 先卸载再删除
                os.popen("/opt/homebrew/bin/ideviceinstaller -u 20a7adaffd52ebb0f01efea599592e4272297911 -U 'video.test.tools.os'").read()
                os.popen("/opt/homebrew/bin/ideviceinstaller -u 20a7adaffd52ebb0f01efea599592e4272297911 -i '%s'" % package_path).read()
                os.remove(r"%s" % package_path)
            # 在这里决定执行哪个包的yaml文件
            if "daily" in file_name_list[0].lower():
                cls.channel = "daily"
            else:
                pass
        except Exception as e:
            print(e)
            raise

    @classmethod
    def restartApp(cls):
        # 重启app
        if cls.device == "ios":
            caps = {}
            caps["platformName"] = "iOS"
            caps["platformVersion"] = "14.6"
            caps["deviceName"] = "iPhone(2)"
            caps["app"] = "video.test.tools.os"
            caps["udid"] = "20a7adaffd52ebb0f01efea599592e4272297911"
            # caps["udid"] = "auto"
            caps['xcodeOrgId'] = '3L4QK9YSAV'
            caps['xcodeSigningId'] = "iPhone Developer"
            caps['autoAcceptAlerts'] = True

            cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            cls.driver.implicitly_wait(10)
            cls.deal_guideAndPop(cls.driver)
            return cls.driver
