#  encoding: utf-8
import sys
import time

import pytest
import allure

from Page.App import App
from Utils.Assert import Assert

@allure.feature("其他功能测试用例")
class TestMyVideo():

    def setup(self):
        # 执行用例前重启app
        self.pureMain = App.main()

    def teardown(self):
        # 截图
        self.pureMain.save_screenShot()

    def test_first_changeChannel(self):
        # 首次启动处理导航
        self.pureMain.dealGuide()
        MePage = self.pureMain.goto_Me()
        MePage.changeChannel("auto_test")

    @allure.story("广告位测试")
    def test_end_CheckAds(self):
        MePage = self.pureMain.goto_Me()
        MePage.changeChannel("ad_test")
        self.pureMain = App.main()
        ad_list =[]
        ad_map = ["Featured", "Trending", "Search_Result", "Search_History", "Detail", "Back_to_app"]
        for page in ad_map:
            result = self.pureMain.findAds(page)
            if result:
                ad_list.append(page)
        if len(ad_list) < len(ad_map):
            print("部分广告位没有找到，%s" % list(set(ad_map).difference(set(ad_list))))
            Assert().assert_equal("部分广告位没有找到", str(set(ad_map).difference(set(ad_list))))

    @allure.story("vip用例")
    def test_end_Vip(self):
        VipPage = self.pureMain.clickVipIcon()
        Assert().assert_equal(True, VipPage.is_exits("Restore"))
        VipPage.closePage()
        Assert().assert_equal(True, VipPage.is_exits("No, thanks"))
        VipPage.clickNoThanks()
        MePage = self.pureMain.goto_Me()
        VipPage = MePage.clickVip()
        Assert().assert_equal(True, VipPage.is_exits("Restore"))
        VipPage.clickContinue()
        Assert().assert_equal(True, self.pureMain.is_exits("Subscribe"))
        VipPage.CancelPay()
        time.sleep(0.5)
        Assert().assert_equal(False, self.pureMain.is_exits("Subscribe"))
        VipPage.clickTerms()
        Assert().assert_equal(True, VipPage.is_exits("Terms & Conditions"))
        self.pureMain.backButton()
        VipPage.clickEULA()
        Assert().assert_equal(True, VipPage.is_exits(
            "This End-User License Agreement (“EULA”) is a legal agreement between you and Pure Tuber."))
        self.pureMain.backButton()
        VipPage.clickRestore()
        time.sleep(5)
        self.pureMain.DeiverWaitDisappear("id", "Restore")
        MePage = self.pureMain.goto_Me()
        Assert().assert_equal(True, MePage.is_exits("All ads blocked for you"))
        # 查免广告
        self.pureMain.goto_Home()
        ad_list = []
        ad_map = ["Detail"]
        for page in ad_map:
            result = self.pureMain.findAds(page)
            if result:
                ad_list.append(page)
        Assert().assert_equal(0, len(ad_list))