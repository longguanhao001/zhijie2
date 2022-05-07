from Page.BasePage import BasePage


class SearchPage(BasePage):
    def get_videoTitle(self):
        # 获取视频标题
        return self.loadSteps("../Data/$channel/SearchPage.yaml", "get_videoTitle")