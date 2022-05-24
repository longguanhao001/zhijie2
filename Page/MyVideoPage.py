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
        return self

    def turnOffHistory(self):
        # 关闭播放历史功能
        self.loadSteps(self.yaml_path, "turnOffHistory")
        return self

    def clickHistory(self):
        # 点击历史按钮
        self.loadSteps(self.yaml_path, "clickHistory")
        return self

    def turnOnHistory(self):
        # 打开播放历史功能
        self.loadSteps(self.yaml_path, "turnOnHistory")
        return self
    
    def goto_Main(self):
        # 关闭播放历史功能
        self.loadSteps(self.yaml_path, "goto_Main")

    def clickSubscribe(self):
        # 点击Subscribe
        self.loadSteps(self.yaml_path, "clickSubscribe")
        return self

    def clickChannel(self, var1):
        # 点击关注页里对应的channel
        self.loadSteps(self.yaml_path, "clickChannel", channelName=var1)
        return self

    def unSubscribePage(self):
        # 取消关注
        self.loadSteps(self.yaml_path, "unSubscribePage")
        return self

    def clickPlaylist(self):
        # 点击Playlist
        self.loadSteps(self.yaml_path, "clickPlaylist")

    def clickSign_in(self):
        # 点击Sign in
        self.loadSteps(self.yaml_path, "clickSign_in")

    def LoginPageBack(self):
        # 点击Sign in
        self.loadSteps(self.yaml_path, "LoginPageBack")

    def delOneHistory(self):
        # 删除一个播放历史
        self.loadSteps(self.yaml_path, "delOneHistory")

    def delAllHistory(self):
        # 删除所有播放历史
        self.loadSteps(self.yaml_path, "delAllHistory")

    def closeHistory(self):
        #关闭播放历史功能
        self.loadSteps(self.yaml_path, "closeHistory")

    def openHistory(self):
        #打开播放历史功能
        self.loadSteps(self.yaml_path, "openHistory")

    def clickWatchLater(self):
        # 点击watchlater
        self.loadSteps(self.yaml_path, "clickWatchLater")
        return self

    def RandomPlay(self):
        # 随机播放watchlater
        self.loadSteps(self.yaml_path, "RandomPlay")
        return self

    def PlayAll(self):
        # 全部播放watchlater
        self.loadSteps(self.yaml_path, "PlayAll")
        return self

    def clickVideo(self):
        # 点击视频cell
        self.loadSteps(self.yaml_path, "clickVideo")
        return self

    def removeVideo(self):
        # 删除watch later
        self.loadSteps(self.yaml_path, "removeVideo")
        return self