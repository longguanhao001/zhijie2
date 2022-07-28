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


