from Page.BasePage import BasePage


class MyVideoPage(BasePage):
    yaml_path = "../Data/$channel/MyVideoPage.yaml"

    def getVideoName(self):
        # 获取视频标题
        return self.loadSteps(self.yaml_path, "getVideoName")

    def goto_VideoDetail(self):
        # 获取视频标题
        self.loadSteps(self.yaml_path, "goto_VideoDetail")

    def cleanHistory(self):
        # 清理播放历史
        self.loadSteps(self.yaml_path, "cleanHistory")

    def turnOffHistory(self):
        # 关闭播放历史功能
        self.loadSteps(self.yaml_path, "turnOffHistory")
        return self

    def goto_Main(self):
        # 关闭播放历史功能
        self.loadSteps(self.yaml_path, "goto_Main")

    def clickSubscribe(self):
        # 点击Subscribe
        self.loadSteps(self.yaml_path, "clickSubscribe")

    def clickPlaylist(self):
        # 点击Playlist
        self.loadSteps(self.yaml_path, "clickPlaylist")

    def clickSign_in(self):
        # 点击Sign in
        self.loadSteps(self.yaml_path, "clickSign_in")

    def LoginPageBack(self):
        # 点击Sign in
        self.loadSteps(self.yaml_path, "LoginPageBack")