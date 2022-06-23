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
        return self.loadSteps(self.yaml_path, "channelClickVideo")

    def clickchannel(self):
        # 跳转到channel页
        self.loadSteps(self.yaml_path, "clickchannel")
        return self

    def clickVideosTag(self):
        # 在channel页中点击videos tag
        return self.loadSteps(self.yaml_path, "clickVideosTag")

    def channelSortBy(self, var1):
        # 在channel页中排序视频
        return self.loadSteps(self.yaml_path, "channelSortBy", key=var1)


    def goto_Search(self, var1=None):
        # 跳转到me页
        self.loadSteps(self.yaml_path, "goto_Search", keyword=var1)
        return SearchPage()

    def changeTag(self, var1):
        # 跳转到me页
        self.loadSteps(self.yaml_path, "changeTag", TagName=var1)
        return self

    def goto_VideoDetail(self):
        # 跳转到视频详情页
        self.loadSteps(self.yaml_path, "goto_VideoDetail")
        return VideoDetailPage()

    def goto_MyVideo(self):
        # 跳转到视频详情页
        self.loadSteps(self.yaml_path, "goto_MyVideo")
        return MyVideoPage()

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