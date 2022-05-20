#  encoding: utf-8
import sys
import time

sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")

import allure

from Page.App import App
from Utils.Assert import Assert

@allure.feature("Me页测试用例")
class TestMe():

    def setup(self):
        # 执行用例前重启app
        self.pureMain = App.main()

    def teardown(self):
        # 截图
        self.pureMain.save_screenShot()

    @allure.story("未登录时点击小铃铛会跳转到登陆页")
    def test_bell_unlogin(self):
        MePage = self.pureMain.goto_Me()
        time.sleep(3)
        MePage.clickBell()
        time.sleep(3)
        Assert().assert_in("Email or phone", MePage.driver.page_source)

    @allure.story("分享app链接")
    def test_shareApp(self):
        MePage = self.pureMain.goto_Me()
        MePage.share_app()
        MePage.clickSign_in().clipboardValue()
        time.sleep(0.5)
        Assert().assert_in("id1594183379", MePage.driver.page_source)

    @allure.story("反馈功能测试")
    def test_feedback(self):
        MePage = self.pureMain.goto_Me()
        MePage.feedback("iosautotest feedback")
        time.sleep(0.2)
        Assert().assert_in("send success", MePage.driver.page_source)

    @allure.story("协议页检查")
    def test_policy(self):
        MePage = self.pureMain.goto_Me().clickPolicy()
        time.sleep(0.5)
        Assert().assert_in("Privacy Policy", MePage.driver.page_source)


