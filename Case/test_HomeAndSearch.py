#  encoding: utf-8
import sys

sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")

import allure

from Page.App import App
from Utils.Assert import Assert


@allure.feature("首页和搜索页测试用例")
class TestPure():

    def setup(self):
        # 每次执行用例重启app
        self.pureMain = App.main()

    def teardown(self):
        # 截图
        self.pureMain.save_screenShot()

    @allure.story("搜索测试用例")
    @allure.step("搜索正常内容")
    def test_search_nomal(self):
        # 搜索非18+内容
        allure.step("搜索非18+内容")
        keyword = "dualipa"
        video_title = self.pureMain.goto_Search(keyword).get_videoTitle()
        Assert().assert_in(keyword, video_title.lower().replace(" ", ""))

    @allure.story("搜索测试用例")
    @allure.step("搜索18+内容")
    def test_search_18(self):
        # 搜索18+内容
        keyword = "sex"
        SearchPage = self.pureMain.goto_Search(keyword)
        sex_video = ["Cheat Codes x Kris Kross Amsterdam - SEX (Official Music Video)", "Full hindi sex video in bathroom",
                     "Sex in Public Prank - GONE SEXUAL", "Is She Going Too Far? | Sex Madness", "ASKING GUYS FOR SEX (SOCIAL EXPERIMENT)"]
        for i in range(5):
            video_title = SearchPage.get_videoTitle()
            Assert().assert_not_in(video_title, sex_video)
            self.pureMain.swipe("up")

    @allure.story("搜索测试用例")
    @allure.step("搜索屏蔽内容")
    def test_search_blackworld(self):
        # 搜索屏蔽内容
        keyword = "zing"
        video_title = self.pureMain.goto_Search(keyword).get_videoTitle()
        Assert().assert_not_in(keyword, video_title.lower())

    @allure.story("Home页测试用例")
    def test_HomeTag(self):
        #检查home tag切换功能
        video_title_list = []
        video_title_list.append(self.pureMain.getVideoName())
        for i in ["Trending", "Music", "Gaming", "Movies"]:
            video_title = self.pureMain.changeTag(i).getVideoName()
            Assert().assert_not_in(video_title, video_title_list)
            video_title_list.append(video_title)




