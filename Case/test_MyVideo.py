#  encoding: utf-8
import sys
import time

sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")

import allure

from Page.App import App
from Utils.Assert import Assert

@allure.feature("资产页测试用例")
class TestMyVideo():

    def setup(self):
        # 执行用例前重启app
        self.pureMain = App.main()

    def teardown(self):
        # 截图
        self.pureMain.save_screenShot()

    @allure.story("本地播放历史")
    def test_LocalHistory(self):
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(10)
        DetailPage.closeVideo()
        MyVideoPage = self.pureMain.goto_MyVideo()
        cur_videoName = MyVideoPage.getVideoName()
        MyVideoPage.cleanHistory()
        Assert().assert_not_in(cur_videoName, MyVideoPage.driver.page_source)

        MyVideoPage.turnOffHistory().goto_Main()
        homeVideoName = self.pureMain.getVideoName()
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(5)
        DetailPage.closeVideo()
        self.pureMain.goto_MyVideo()
        self.pureMain.swipe("down")
        MyVideoPage.turnOnHistory() # 打开播放历史避免影响其他用例
        Assert().assert_not_in(homeVideoName, MyVideoPage.driver.page_source)

    @allure.story("未登录时点击这些按钮会跳转到登陆页")
    def test_unlogin(self):
        MyVideoPage = self.pureMain.goto_MyVideo()
        time.sleep(3)
        MyVideoPage.clickSubscribe()
        time.sleep(3)
        Assert().assert_in("Email or phone", MyVideoPage.driver.page_source)
        MyVideoPage.LoginPageBack()
        time.sleep(1)
        MyVideoPage.clickPlaylist()
        time.sleep(3)
        Assert().assert_in("Email or phone", MyVideoPage.driver.page_source)
        MyVideoPage.LoginPageBack()
        time.sleep(1)
        MyVideoPage.clickSign_in()
        time.sleep(3)
        Assert().assert_in("Email or phone", MyVideoPage.driver.page_source)
        MyVideoPage.LoginPageBack()




