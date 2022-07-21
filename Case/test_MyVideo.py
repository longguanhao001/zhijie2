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
        Assert().assert_equal(False, self.pureMain.is_exits(cur_videoName))

        MyVideoPage.turnOffHistory().goto_Main()
        homeVideoName = self.pureMain.getVideoName()
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(5)
        DetailPage.closeVideo()
        self.pureMain.goto_MyVideo()
        self.pureMain.swipe("down")
        Assert().assert_equal(False, self.pureMain.is_exits(homeVideoName))
        MyVideoPage.turnOnHistory() # 打开播放历史避免影响其他用例

    @allure.story("未登录时点击这些按钮会跳转到登陆页")
    def test_unlogin(self):
        MyVideoPage = self.pureMain.goto_MyVideo()
        time.sleep(1)
        MyVideoPage.clickSubscribe()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits("Email or phone"))
        MyVideoPage.LoginPageBack()
        time.sleep(1)
        MyVideoPage.clickSign_in()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits("Email or phone"))
        MyVideoPage.LoginPageBack()

    @allure.story("订阅列表用例")
    def test_Subscribe_login(self):
        # 关注
        channelName = self.pureMain.getChannelName()
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(3)
        DetailPage.subsribe().closeVideo()
        MyVideoPage = self.pureMain.goto_MyVideo()
        time.sleep(3)
        SubscribePage = MyVideoPage.clickSubscribe()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits(channelName))
        MyVideoPage.clickALL()
        # 取关
        while SubscribePage.is_exits_channel():
            channelDetailPage = SubscribePage.clickChannel()
            channelDetailPage.unSubscribePage()
            time.sleep(2)
            self.pureMain.backButton()
            time.sleep(1)
            self.pureMain.swipe("down")
        Assert().assert_equal(False, self.pureMain.is_exits(channelName))

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
        Assert().assert_equal(True, self.pureMain.is_exits(homeVideoName))

        HistoryVideoName = HistoryPage.getVideoName()
        HistoryPage.delOneHistory()
        time.sleep(1)
        Assert().assert_equal(False, self.pureMain.is_exits(HistoryVideoName))

        HistoryPage.delAllHistory()
        time.sleep(1)
        Assert().assert_equal(True, self.pureMain.is_exits("No Videos"))

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
        Assert().assert_equal(False, self.pureMain.is_exits(homeVideoName))
        HistoryPage.openHistory()

    @allure.story("WatchLater功能用例")
    def test_WatchLater_login(self):
        homeVideoName = self.pureMain.getVideoName()
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(3)
        DetailPage.add_to().Watchlater().closeVideo()
        MyVideoPage = self.pureMain.goto_MyVideo()
        WatchLaterPage = MyVideoPage.clickWatchLater()
        Assert().assert_equal(True, self.pureMain.is_exits(homeVideoName))
        WatchLaterPage.RandomPlay()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits("Add to"))
        DetailPage.closeVideo()

        WatchLaterPage.PlayAll()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits("Add to"))
        DetailPage.closeVideo()

        WatchLaterPage.clickVideo()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits("Add to"))
        DetailPage.closeVideo()

        WatchLaterPage.removeVideo()
        time.sleep(2)
        Assert().assert_equal(False, self.pureMain.is_exits(homeVideoName))

    @allure.story("LikedVideos功能用例")
    def test_LikedVideo_login(self):
        homeVideoName1 = self.pureMain.getVideoName()
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(3)
        DetailPage.like().closeVideo()

        self.pureMain.swipe("up")
        homeVideoName2 = self.pureMain.getVideoName()
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(3)
        DetailPage.like().closeVideo()

        MyVideoPage = self.pureMain.goto_MyVideo()
        time.sleep(1)
        LikeVideosPage = MyVideoPage.clickLikeVideos()
        Assert().assert_equal(True, self.pureMain.is_exits(homeVideoName1))
        LikeVideosPage.RandomPlay()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits("Add to"))
        DetailPage.closeVideo()

        LikeVideosPage.PlayAll()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits("Add to"))
        DetailPage.closeVideo()

        LikeVideosPage.removeVideo()
        time.sleep(0.5)
        Assert().assert_equal(False, self.pureMain.is_exits(homeVideoName2))

        LikeVideosPage.clickVideo()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits("Add to"))
        DetailPage.dislike().closeVideo()
        self.pureMain.swipe("down")
        Assert().assert_equal(False, self.pureMain.is_exits(homeVideoName1))




    @allure.story("PlayList功能用例")
    def test_Playlist_login(self):
        homeVideoName = self.pureMain.getVideoName()
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(3)
        DetailPage.add_to().Playlist().closeVideo()
        MyVideoPage = self.pureMain.goto_MyVideo()
        PlaylistPage = MyVideoPage.clickPlaylist()
        Assert().assert_equal(True, self.pureMain.is_exits(homeVideoName))
        PlaylistPage.RandomPlay()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits("Add to"))
        DetailPage.closeVideo()

        PlaylistPage.PlayAll_Share()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits("Add to"))
        DetailPage.closeVideo()

        PlaylistPage.clickVideo()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits("Add to"))
        DetailPage.closeVideo()
        while 1: # 删除全部视频
            try:
                PlaylistPage.removeVideo()
                time.sleep(0.5)
            except:
                break
        Assert().assert_equal(False, self.pureMain.is_exits(homeVideoName))
