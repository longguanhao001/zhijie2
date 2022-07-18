#  encoding: utf-8
import sys
import time

import pytest

sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")

import allure

from Page.App import App
from Utils.Assert import Assert

@allure.feature("视频详情页测试用例")
class TestVideoDetail():

    def setup(self):
        # 执行用例前重启app
        self.pureMain = App.main()

    def teardown(self):
        # 截图
        self.pureMain.save_screenShot()

    @allure.story("视频详情页测试用例")
    @allure.step("未登录时跳转")
    def test_videoDetail_unlogin(self):
        # 暂停、下一首、上一首、切换画质、切换速度等功能变化性较大容错性低，不做自动化测试
        # 点赞、点踩、关注、add_to
        DetailPage = self.pureMain.goto_VideoDetail()
        DetailPage.like()
        Assert().assert_not_in("Add to", DetailPage.driver.page_source)
        DetailPage.LoginPageBack()

        DetailPage.dislike()
        Assert().assert_not_in("Add to", DetailPage.driver.page_source)
        DetailPage.LoginPageBack()

        DetailPage.add_to()
        Assert().assert_not_in("Add to", DetailPage.driver.page_source)
        DetailPage.LoginPageBack()

        DetailPage.subsribe()
        Assert().assert_not_in("Add to", DetailPage.driver.page_source)
        DetailPage.LoginPageBack()

    @allure.story("视频详情页测试用例")
    @allure.step("upnext功能")
    def test_upnext(self):
        # upnext
        DetailPage = self.pureMain.goto_VideoDetail()
        cur_likeCount = DetailPage.getLikeCount()
        upnextVideoList = []
        for i in range(3):
            self.pureMain.swipe("up")
            self.pureMain.swipe("up")
            videoName = DetailPage.getUpnextVideoName()
            Assert().assert_not_in(videoName, upnextVideoList)
            upnextVideoList.append(videoName)
        DetailPage.clickUpnext()
        time.sleep(1)
        new_likeCount = DetailPage.getLikeCount()
        Assert().assert_not_equal(cur_likeCount, new_likeCount)

    @allure.story("视频详情页测试用例")
    @allure.step("local history功能")
    def test_playhistory_unlogin(self):
        homeVideoName = self.pureMain.getVideoName()
        DetailPage = self.pureMain.goto_VideoDetail()
        time.sleep(10)
        min, sec = str(DetailPage.get_nowProgress()).split(":")
        cur_Progress = int(min)*60+int(sec)
        DetailPage.closeVideo()
        MyVideoPage = self.pureMain.goto_MyVideo()
        Assert().assert_equal(True, self.pureMain.is_exits(homeVideoName))
        MyVideoPage.goto_VideoDetail()
        time.sleep(10)
        while 1:  # 等待视频加载完成
            DetailPage.clickVideo()
            if self.pureMain.is_exits("videoDetail player pauseBtn"):
                break
            else:
                time.sleep(5)
        min, sec = str(DetailPage.get_nowProgress()).split(":")
        now_Progress = int(min) * 60 + int(sec)
        Assert().assert_greaterAndEqual(now_Progress, cur_Progress)

    # @allure.story("视频详情页测试用例")
    # @allure.step("local history功能")
    # def test_playhistory_unlogin1(self):
    #     homeVideoName = self.pureMain.getVideoName()
    #     DetailPage = self.pureMain.goto_VideoDetail()
    #     time.sleep(6)
    #     cur_Progress = str(DetailPage.get_nowProgress1())
    #     while int(cur_Progress) < 1:
    #         time.sleep(6)
    #         cur_Progress = str(DetailPage.get_nowProgress1())
    #     DetailPage.closeVideo()
    #     MyVideoPage = self.pureMain.goto_MyVideo()
    #     Assert().assert_equal(True, self.pureMain.is_exits(homeVideoName))
    #     MyVideoPage.goto_VideoDetail()
    #     time.sleep(5)
    #     while 1:  # 等待视频加载完成
    #         DetailPage.clickVideo()
    #         if self.pureMain.is_exits("videoDetail player pauseBtn"):
    #             break
    #         else:
    #             time.sleep(5)
    #     now_Progress = str(DetailPage.get_nowProgress1())
    #     Assert().assert_greaterAndEqual(now_Progress, cur_Progress)
