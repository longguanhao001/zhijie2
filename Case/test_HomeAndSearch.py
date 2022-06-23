#  encoding: utf-8
import sys
import time

import pytest

sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")

import allure

from Page.App import App
from Utils.Assert import Assert


@allure.feature("首页和搜索页测试用例")
class TestHomeSearch():

    def setup(self):
        # 每次执行用例重启app
        self.pureMain = App.main()

    def teardown(self):
        # 截图
        self.pureMain.save_screenShot()

    @allure.story("搜索测试用例")
    def test_search(self):
        # 搜索非18+内容
        allure.step("搜索非18+内容")
        keyword = "dualipa"
        video_title = self.pureMain.goto_Search(keyword).get_videoTitle()
        Assert().assert_in(keyword, video_title.lower().replace(" ", ""))

        # 搜索色情内容
        self.pureMain.backButton()
        keyword = "sex"
        SearchPage = self.pureMain.goto_Search(keyword)
        sex_video = ["Cheat Codes x Kris Kross Amsterdam - SEX (Official Music Video)", "Full hindi sex video in bathroom",
                     "Sex in Public Prank - GONE SEXUAL", "Is She Going Too Far? | Sex Madness", "ASKING GUYS FOR SEX (SOCIAL EXPERIMENT)"]
        for i in range(5):
            video_title = SearchPage.get_videoTitle()
            Assert().assert_not_in(video_title, sex_video)
            self.pureMain.swipe("up")

        # 搜索屏蔽词
        self.pureMain.backButton()
        keyword = "zing"
        video_title = self.pureMain.goto_Search(keyword).get_videoTitle()
        Assert().assert_not_in(keyword, video_title.lower())

    @allure.story("Home页测试用例")
    def test_HomeTag(self):
        #检查home tag切换功能
        for i in ["Trending", "Music", "Gaming", "Movies"]:
            video_title = self.pureMain.changeTag(i).getVideoName()
            Assert().assert_not_equal(None, video_title)

    @allure.story("Home页mor按钮功能测试用例")
    def test_more_login(self):

        # 举报内容
        self.pureMain.clickMore().clickReportContent().selectAndReport("Sexual content")
        Assert().assert_equal(True, self.pureMain.is_exits("Report Success"))

        # 背景播放
        video_name = self.pureMain.getVideoName()
        self.pureMain.clickMore()
        Assert().assert_equal(True, self.pureMain.is_exits("Report Content"))
        self.pureMain.clickBgPlay()
        Assert().assert_equal(True, self.pureMain.is_exits("Tab Bar")) # 断言是否后台播放
        self.pureMain.closeVideo()

        # 分享
        self.pureMain.clickMore().clickShare()
        self.pureMain.click_Search().clipboardValue()
        Assert().assert_in(video_name, self.pureMain.driver.page_source)
        self.pureMain.backButton()


        # no interested
        self.pureMain.clickMoreTwo().clickNotInterested()
        Assert().assert_equal(True, self.pureMain.is_exits("Video removed"))
        self.pureMain.NotInterestedUndo()
        time.sleep(1)
        Assert().assert_equal(False, self.pureMain.is_exits("Video removed"))

        # 加入playlist和稍后看
        self.pureMain.clickMore().clickAddToPlaylist()
        self.pureMain.clickMore().clickAddToWatchLater()
        PlaylistPage = self.pureMain.goto_MyVideo().clickPlaylist()
        Assert().assert_equal(True, self.pureMain.is_exits(video_name))
        PlaylistPage.removeVideo(video_name)
        self.pureMain.backButton()
        PlaylistPage.clickWatchLater()
        Assert().assert_equal(True, self.pureMain.is_exits(video_name))
        PlaylistPage.removeVideo(video_name)
        self.pureMain.backButton().goto_Home()

        # 小窗播放
        self.pureMain.clickMore().clickPopPlay()
        Assert().assert_equal(True, self.pureMain.is_exits("PIPUIView"))  # 断言是否小窗播放

    @allure.story("channel页功能测试用例")
    def test_channel(self):
        # channel页功能
        ChannelPage = self.pureMain.clickchannel()
        Assert().assert_equal(True, self.pureMain.is_exits("Report"))

        # 播放视频
        DetailPage = ChannelPage.channelClickVideo()
        time.sleep(3)
        Assert().assert_equal(True, self.pureMain.is_exits("Add to"))
        DetailPage.closeVideo()

        # 其他页面ß
        ChannelPage.clickAboutlTag()
        ChannelPage.clickChannelTag()

        # 播放视频
        ChannelPage.clickVideosTag()
        Assert().assert_equal(True, self.pureMain.is_exits("Sort by"))
        if self.pureMain.is_exits("Sort by"):
            for i in ["Most popular", "Date added (oldest)", "Date added (newest)"]:
                ChannelPage.channelSortBy(i)
        ChannelPage.channelClickVideo()
        Assert().assert_equal(True, self.pureMain.is_exits("Add to"))
        DetailPage.closeVideo()

        # 播放playlist
        ChannelPage.clickPlaylistsTag()
        if self.pureMain.is_exits("Sort by"):
            for i in ["Last video added", "Date added (newest)"]:
                ChannelPage.channelSortBy(i)
        ChannelPage.channelClickPlaylist()
        Assert().assert_equal(True, self.pureMain.is_exits("Add to"))
        DetailPage.closeVideo()
        self.pureMain.backButton()








