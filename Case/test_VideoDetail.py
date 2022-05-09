#  encoding: utf-8
import sys
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")
import allure

from Page.App import App
from Utils.Assert import Assert


class TestVideoDetail():

    @classmethod
    def setup_class(cls):
        # 执行用例前重启app
        cls.pureMain = App.main()

    @allure.story("视频详情页测试用例")
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

    def test_upnext(self):
        # upnext
        DetailPage = self.pureMain.goto_VideoDetail()
        cur_likeCount = DetailPage.getLikeCount()
        upnextVideoList = []
        for i in range(8):
            self.pureMain.swipe("up")
            videoName = DetailPage.getUpnextVideoName()
            Assert().assert_not_in(videoName, upnextVideoList)
            upnextVideoList.append(videoName)
        DetailPage.clickUpnext()
        new_likeCount = DetailPage.getLikeCount()
        Assert().assert_not_equal(cur_likeCount, new_likeCount)