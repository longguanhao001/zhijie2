#  encoding: utf-8
import sys
import time

import pytest

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

    @allure.story("订阅列表用例")
    def test_Subscribe_login(self):
        # 关注
        channelName = self.pureMain.getChannelName()
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(3)
        DetailPage.subsribe().closeVideo()
        MyVideoPage = self.pureMain.goto_MyVideo()
        time.sleep(1)
        SubscribePage = MyVideoPage.clickSubscribe()
        time.sleep(1)
        Assert().assert_in(channelName, SubscribePage.driver.page_source)

        # 取关
        channelDetailPage = SubscribePage.clickChannel(channelName)
        channelDetailPage.unSubscribePage()
        self.pureMain.backButton().swipe("down")
        time.sleep(1)
        Assert().assert_not_in(channelName, SubscribePage.driver.page_source)

    @allure.story("播放历史用例")
    def test_History_login(self):
        # 记录历史功能打开时
        homeVideoName = self.pureMain.getVideoName()
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(3)
        self.pureMain.swipe("up")
        DetailPage.clickUpnext()
        time.sleep(3)
        DetailPage.closeVideo()
        MyVideoPage = self.pureMain.goto_MyVideo()
        time.sleep(1)
        HistoryPage = MyVideoPage.clickHistory()
        time.sleep(1)
        Assert().assert_in(homeVideoName, HistoryPage.driver.page_source)

        HistoryVideoName = HistoryPage.getVideoName()
        HistoryPage.delOneHistory()
        time.sleep(1)
        Assert().assert_not_in(HistoryVideoName, HistoryPage.driver.page_source)

        HistoryPage.delAllHistory()
        time.sleep(1)
        Assert().assert_in("No Videos", HistoryPage.driver.page_source)
        # 记录历史功能关闭时
        HistoryPage.closeHistory()
        self.pureMain.backButton().goto_Home()
        homeVideoName = self.pureMain.getVideoName()
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(3)
        DetailPage.closeVideo()
        MyVideoPage = self.pureMain.goto_MyVideo()
        time.sleep(1)
        HistoryPage = MyVideoPage.clickHistory()
        time.sleep(1)
        Assert().assert_not_in(homeVideoName, HistoryPage.driver.page_source)
        HistoryPage.openHistory()

    @allure.story("WatchLater功能用例")
    def test_WatchLater_login(self):
        homeVideoName = self.pureMain.getVideoName()
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(3)
        DetailPage.add_to().Watchlater().closeVideo()
        MyVideoPage = self.pureMain.goto_MyVideo()
        WatchLaterPage = MyVideoPage.clickWatchLater()
        Assert().assert_in(homeVideoName, WatchLaterPage)
        WatchLaterPage.RandomPlay()
        time.sleep(3)
        Assert().assert_in("Add to", WatchLaterPage.driver.page_source)
        DetailPage.closeVideo()

        WatchLaterPage.PlayAll()
        time.sleep(3)
        Assert().assert_in("Add to", WatchLaterPage.driver.page_source)
        DetailPage.closeVideo()

        WatchLaterPage.clickVideo()
        time.sleep(3)
        Assert().assert_in("Add to", WatchLaterPage.driver.page_source)
        DetailPage.closeVideo()

        WatchLaterPage.removeVideo()
        time.sleep(0.5)
        Assert().assert_not_in(homeVideoName, WatchLaterPage.driver.page_source)








