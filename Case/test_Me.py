#  encoding: utf-8
import sys
import time

sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")

import allure
import pytest
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
        # reuslt = self.pureMain.DeiverWaitToast("Send success") # 显示等待toast不管用
        time.sleep(2)
        Assert().assert_not_equal("Create", MePage.driver.page_source)

    @allure.story("协议页检查")
    def test_policy(self):
        MePage = self.pureMain.goto_Me().clickPolicy()
        time.sleep(1.5)
        Assert().assert_in("Privacy Policy", str(MePage.driver.page_source))

    @allure.story("登录用例")
    def test_login(self):
        MePage = self.pureMain.goto_Me()
        time.sleep(3)
        if App().is_test() == True:
            account = "vivopurehu"
            password = "zxcv4321"
            name = "Vivopure Hu"
            MePage.clickSign_in().login(account, password)
        else:
            # ccount = "vivopurehu"
            # password = "zxcv4321"
            name = "Vivopure Hu"
            # MePage.clickSign_in().login("正式账号")
        time.sleep(10)
        username = MePage.getUserName()
        Assert().assert_equal(name, username)

    @allure.story("登录后点击小铃铛")
    def test_bell_login(self):
        MePage = self.pureMain.goto_Me()
        MePage.clickBell()
        time.sleep(0.5)
        Assert().assert_in("Notifications", self.pureMain.driver.page_source)
        MePage.clickReply()
        time.sleep(0.5)
        Assert().assert_in("Comments", self.pureMain.driver.page_source)
        MePage.clickComment()
        time.sleep(0.5)
        Assert().assert_in("Replies", self.pureMain.driver.page_source)
        MePage.reply("i reply you")
        # self.pureMain.DeiverWaitToast("delete grey box")
        time.sleep(1)
        Assert().assert_in("delete grey box", self.pureMain.driver.page_source)
        MePage.delReply()
        time.sleep(0.5)
        Assert().assert_not_in("delete grey box", self.pureMain.driver.page_source)
        MePage.clickVideo()
        time.sleep(0.5)
        Assert().assert_not_in("Replies", self.pureMain.driver.page_source)