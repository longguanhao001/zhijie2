#  encoding: utf-8
import sys
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")

import allure

from Page.App import App
from Utils.Assert import Assert


@allure.feature("ios pure 自动化测试")
class TestPure():

    def setup(self):
        # 每次执行用例重启app
        self.pureMain = App.main()

    @allure.story("搜索测试用例")
    def test_search(self):
        # 搜索非18+内容
        keyword = "dualipa"
        video_title = self.pureMain.goto_Search(keyword).get_videoTitle()
        Assert().assert_in(keyword, video_title.lower().replace(" ", ""))
        # 搜索18+内容
