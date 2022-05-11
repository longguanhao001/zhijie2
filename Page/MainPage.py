from Page.BasePage import BasePage
from Page.MePage import MePage
from Page.MyVideoPage import MyVideoPage
from Page.SearchPage import SearchPage
from Page.VideoDetailPage import VideoDetailPage


class MainPage(BasePage):
    yaml_path = "../Data/$channel/MainPage.yaml"

    def goto_Me(self):
        # 跳转到me页
        pass

    def getVideoName(self):
        # 获取home页面的视频标题
        return self.loadSteps(self.yaml_path, "getVideoName")

    def goto_Search(self, var1):
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