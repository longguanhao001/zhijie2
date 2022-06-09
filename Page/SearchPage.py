from Page.BasePage import BasePage


class SearchPage(BasePage):
    yaml_path = "../Data/$channel/SearchPage.yaml"
    def get_videoTitle(self):
        # 获取视频标题
        return self.loadSteps(self.yaml_path, "get_videoTitle")

    def clipboardValue(self):
        # 长按粘贴
        self.loadSteps(self.yaml_path, "clipboardValue")
        return self
