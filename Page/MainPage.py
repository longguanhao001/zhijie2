from Page.BasePage import BasePage
from Page.SearchPage import SearchPage
from Page.VideoDetailPage import VideoDetailPage


class MainPage(BasePage):

    def goto_Me(self):
        # 跳转到me页
        pass

    def getVideoName(self):
        # 获取home页面的视频标题
        return self.loadSteps("../Data/$channel/MainPage.yaml", "getVideoName")

    def goto_Search(self, var1):
        # 跳转到me页
        self.loadSteps("../Data/$channel/MainPage.yaml", "goto_Search", keyword=var1)
        return SearchPage()

    def changeTag(self, var1):
        # 跳转到me页
        self.loadSteps("../Data/$channel/MainPage.yaml", "changeTag", TagName=var1)
        return self

    def goto_VideoDetail(self):
        # 跳转到视频详情页
        self.loadSteps("../Data/$channel/MainPage.yaml", "goto_VideoDetail")
        return VideoDetailPage()