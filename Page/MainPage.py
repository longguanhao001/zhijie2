import time

from Page.BasePage import BasePage
from Page.MePage import MePage
from Page.MyVideoPage import MyVideoPage
from Page.SearchPage import SearchPage
from Page.VideoDetailPage import VideoDetailPage


class MainPage(BasePage):
    yaml_path = "../Data/$channel/MainPage.yaml"

    def getVideoName(self):
        # 获取home页面的视频标题
        return self.loadSteps(self.yaml_path, "getVideoName")

    def getChannelName(self):
        # 获取home页面的视频频道名
        return self.loadSteps(self.yaml_path, "getChannelName")

    def channelClickVideo(self):
        # 跳转到channel页
        self.loadSteps(self.yaml_path, "channelClickVideo")
        return VideoDetailPage()

    def clickchannel(self):
        # 跳转到channel页
        self.loadSteps(self.yaml_path, "clickchannel")
        return self

    def clickVideosTag(self):
        # 在channel页中点击videos tag
        return self.loadSteps(self.yaml_path, "clickVideosTag")

    def channelSortBy(self, var1):
        # 在channel页中排序视频
        return self.loadSteps(self.yaml_path, "channelSortBy", keyword=var1)


    def goto_Search(self, var1=None):
        # 跳转到search页
        self.loadSteps(self.yaml_path, "goto_Search", keyword=var1)
        return SearchPage()

    def changeTag(self, var1):
        # 首页切换tab
        self.loadSteps(self.yaml_path, "changeTag", TagName=var1)
        return self

    def clickPlaylistsTag(self):
        #  在channel页中点击playlist
        self.loadSteps(self.yaml_path, "clickPlaylistsTag")
        return self

    def channelClickPlaylist(self):
        # 在channel页中播放playlist
        self.loadSteps(self.yaml_path, "channelClickPlaylist")
        return self

    def clickChannelTag(self):
        #  在channel页中点击channel tab
        self.loadSteps(self.yaml_path, "clickChannelTag")
        return self

    def clickAboutlTag(self):
        #  在channel页中点击channel tab
        self.loadSteps(self.yaml_path, "clickAboutlTag")
        return self

    def clickSubscribe(self):
        # channel页点击关注
        self.loadSteps(self.yaml_path, "clickSubscribe")
        return self

    def clickUnSubscribe(self):
        # channel页点击不关注
        self.loadSteps(self.yaml_path, "clickUnSubscribe")
        return self

    def goto_VideoDetail(self):
        # 跳转到视频详情页
        self.loadSteps(self.yaml_path, "goto_VideoDetail")
        return VideoDetailPage()

    def goto_MyVideo(self):
        # 跳转到视频详情页
        self.loadSteps(self.yaml_path, "goto_MyVideo")
        return MyVideoPage()

    def dealGuide(self):
        if self.is_exits("Next"):
            self.loadSteps(self.yaml_path, "dealGuide")
        if self.is_exits("Later"):
            self.loadSteps(self.yaml_path, "clickLater")
        return self

    def goto_Me(self):
        # 跳转到我的页
        self.loadSteps(self.yaml_path, "goto_Me")
        return MePage()

    def goto_Home(self):
        # 跳转到我的页
        self.loadSteps(self.yaml_path, "goto_Home")
        return MePage()

    def backButton(self):
        # 主页返回按钮
        self.loadSteps(self.yaml_path, "backButton")
        return self

    def clickMore(self):
        # 主页点击more按钮
        self.loadSteps(self.yaml_path, "clickMore")
        return self

    def clickMoreTwo(self):
        # 主页点击第二个more按钮
        self.loadSteps(self.yaml_path, "clickMoreTwo")
        return self

    def clickBgPlay(self):
        # 主页点击背景播放按钮
        self.loadSteps(self.yaml_path, "clickBgPlay")
        return self

    def clickPopPlay(self):
        # 主页点击小窗播放按钮
        self.loadSteps(self.yaml_path, "clickPopPlay")
        return self

    def clickShare(self):
        # 主页点击分享按钮
        self.loadSteps(self.yaml_path, "clickShare")
        return self

    def click_Search(self):
        # 点击搜索框
        self.loadSteps(self.yaml_path, "click_Search")
        return SearchPage()

    def closeVideo(self):
        # 首页关闭视频
        self.loadSteps(self.yaml_path, "closeVideo")
        return self

    def clickReportContent(self):
        # 首页点击举报
        self.loadSteps(self.yaml_path, "clickReportContent")
        return self

    def clickNotInterested(self):
        # 首页点击NotInterested
        self.loadSteps(self.yaml_path, "clickNotInterested")
        return self

    def selectAndReport(self, var1):
        # 首页举报视频
        self.loadSteps(self.yaml_path, "selectAndReport", option=var1)
        return self

    def AlertClickDone(self):
        # 首页举报弹窗点击done
        self.loadSteps(self.yaml_path, "AlertClickDone")
        return self

    def NotInterestedUndo(self):
        # 撤销NotInterested
        self.loadSteps(self.yaml_path, "NotInterestedUndo")
        return self

    def clickAddToPlaylist(self):
        # 首页加入playlist
        self.loadSteps(self.yaml_path, "clickAddToPlaylist")
        return self

    def clickAddToWatchLater(self):
        # 首页加入playlist
        self.loadSteps(self.yaml_path, "clickAddToWatchLater")
        return self

    def find_FeedAds(self,page):
        for i in range(5):
            try:
                if page != "Search_Result":
                    if page != "Detail":
                        result = self.driver.find_element("xpath","//XCUIElementTypeImage/../XCUIElementTypeButton/XCUIElementTypeStaticText").text
                        # result = self.loadSteps(self.yaml_path, "find_FeedAds")
                    else:
                        result = self.driver.find_element("xpath", "//XCUIElementTypeImage/../../../XCUIElementTypeButton").text
                        # result = self.loadSteps(self.yaml_path, "find_DetailFeedAds")
                else:
                    result = False
                    try:
                        result = self.driver.find_element("xpath", "//XCUIElementTypeTable[@name='Empty list']/../../XCUIElementTypeOther/"
                                                      "XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/"
                                                      "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton").text
                    except:
                        result = self.driver.find_element("//XCUIElementTypeCell /XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton").text
                    # result = self.loadSteps(self.yaml_path, "find_SearchResultAds")
            except:
                result = False
            if result not in ["video icon more", False]:
                return result
            else:
                self.swipe("up")
        return False


    def findAds(self, page):
        # 找各个广告位
        if page == "Featured":
            self.DeiverWaitExist("id", "Trending")
            time.sleep(2)
            result = self.find_FeedAds(page)
        elif page == "Trending":
            self.loadSteps(self.yaml_path, "changeTag", TagName="Trending")
            result = self.find_FeedAds(page)
        elif page == "Search_Result":
            self.loadSteps(self.yaml_path, "goto_Search", keyword="dulipa")
            result = self.find_FeedAds(page)
            self.backButton()
        elif page == "Search_History":
            self.loadSteps(self.yaml_path, "click_Search")
            try:
                result = self.driver.find_element("id", "web dialog").text
                # result = self.loadSteps(self.yaml_path, "find_HistoryAds")
            except:
                result = False
            self.backButton()
        elif page == "Detail":
            self.old_page = self.driver.page_source
            self.loadSteps(self.yaml_path, "goto_VideoDetail")
            time.sleep(15)
            result = self.find_FeedAds(page)
            self.swipe("down")
            self.closeVideo()
            time.sleep(1)
        else:
            new_page = self.driver.page_source
            if new_page == self.old_page:
                result = False
            else:
                result = True
            # try:
            #     # result = self.driver.find_element("id", "PAGDynamicRootView").text
            #     # result = self.loadSteps(self.yaml_path, "find_BackToApp_Ads")
            #     new_page = self.driver.page_source
            #     if new_page == self.old_page:
            #         result = False
            #     else:
            #         result = True
            # except:
            #     result = False
        if result:
            return True
        else:
            return False

    def clickVipIcon(self):
        # 首页面icon入口
        self.loadSteps(self.yaml_path, "clickVipIcon")
        return self

    def closePage(self):
        # 关闭页面
        self.loadSteps(self.yaml_path, "closePage")
        return self

    def clickNoThanks(self):
        # 关闭二次确认弹窗
        if self.is_exits("No, thanks"):
            self.loadSteps(self.yaml_path, "clickNoThanks")
        return self
