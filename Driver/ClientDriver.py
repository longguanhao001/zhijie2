#  encoding: utf-8
import os
import time

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ClientDriver(object):
    driver: WebDriver
    # 后期从jenkins获取的参数
    device = "ios"
    env = "test"
    channel = "pure"

    @classmethod
    def deal_guideAndPop(cls, driver: WebDriver):
        # 处理导航页和更新弹窗
        # 显示等待
        try:
            toast_loc = ("id", "icon x white delete")
            ele = WebDriverWait(driver, 5, 0.3).until(expected_conditions.visibility_of_element_located(toast_loc))
            if ele:
                ele.click()
        except:
            print("启动app无弹窗")

    @classmethod
    def installApp(cls):
        # 安装app
        try:
            result = os.popen("/opt/homebrew/bin/ideviceinstaller -u 20a7adaffd52ebb0f01efea599592e4272297911 -l").read()
            # 获取安装包文件
            path = os.path.dirname(os.getcwd())
            file_name_list = os.listdir("%s/Package" % path)
            cur_path = os.path.dirname(os.getcwd())
            package_path = "%s/Package/%s" % (cur_path, file_name_list[0])
            if "video.test.tools.os" not in result:
                result = os.popen("/opt/homebrew/bin/ideviceinstaller -u 20a7adaffd52ebb0f01efea599592e4272297911 -i '%s'" % package_path).read()
                print(result)
                os.remove(r"%s" % package_path)
            else:
                # 先卸载再删除x
                os.popen("/opt/homebrew/bin/ideviceinstaller -u 20a7adaffd52ebb0f01efea599592e4272297911 -U 'video.test.tools.os'").read()
                result = os.popen("/opt/homebrew/bin/ideviceinstaller -u 20a7adaffd52ebb0f01efea599592e4272297911 -i '%s'" % package_path).read()
                print(result)
                os.remove(r"%s" % package_path)
            # 在这里决定执行哪个包的yaml文件
            if "daily" in file_name_list[0].lower():
                cls.channel = "daily"
            elif "go" in file_name_list[0].lower():
                cls.channel = "go"
            else:
                pass
            print("start test for %s" % cls.channel)
        except Exception as e:
            print("install app error%s"%e)
            pass

    @classmethod
    def restartApp(cls):
        # 重启app
        if cls.device == "ios":
            caps = {}
            caps["platformName"] = "iOS"
            caps["platformVersion"] = "14.6"
            # caps["platformVersion"] = "14.4"
            caps["deviceName"] = "iPhone(2)"
            # caps["deviceName"] = "iPhone"
            caps["app"] = "video.test.tools.os"
            # caps["udid"] = "79ebcfc82ea26c42c13a81371cbc1b8e172488f9"
            caps["udid"] = "20a7adaffd52ebb0f01efea599592e4272297911"
            # caps['xcodeOrgId'] = '3L4QK9YSAV'
            caps['xcodeOrgId'] = '8444HTHN7B'
            caps['xcodeSigningId'] = "iPhone Developer"
            caps['autoAcceptAlerts'] = True
            cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            cls.driver.implicitly_wait(10)
            # cls.deal_guideAndPop(cls.driver)
            # cls.firstopen = False
            return cls.driver
