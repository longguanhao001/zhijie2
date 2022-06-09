from Page.BasePage import BasePage


class VideoDetailPage(BasePage):
    yaml_path = "../Data/$channel/VideoDetailPage.yaml"

    def LoginPageBack(self):
        # 跳转到登陆页后返回
        self.loadSteps(self.yaml_path, "LoginPageBack")

    def get_nowProgress(self):
        # 获取当前视频进度
        return self.loadSteps(self.yaml_path, "get_nowProgress")

    def like(self):
        # 点击点赞按钮
        self.loadSteps(self.yaml_path, "like")
        return self

    def dislike(self):
        # 点击点赞按钮
        self.loadSteps(self.yaml_path, "dislike")
        return self

    def add_to(self):
        # 点击add_to按钮
        self.loadSteps(self.yaml_path, "add_to")
        return self

    def Watchlater(self):
        # 添加视频到watch later
        self.loadSteps(self.yaml_path, "Watchlater")
        return self

    def Playlist(self):
        # 添加视频到Playlist
        self.loadSteps(self.yaml_path, "Playlist")
        return self

    def backGroundPlay(self):
        pass

    def popupPlay(self):
        # 点击点赞按钮
        self.loadSteps(self.yaml_path, "subsribe")

    def Share(self):
        pass

    def subsribe(self):
        # 点击点赞按钮
        self.loadSteps(self.yaml_path, "subsribe")
        return self

    def open_comment(self):
        pass

    def clickUpnext(self):
        # 点击点赞按钮
        self.loadSteps(self.yaml_path, "clickUpnext")

    def getLikeCount(self):
        # 获取点赞数量
        return self.loadSteps(self.yaml_path, "getLikeCount")

    def getUpnextVideoName(self):
        # 获取upnext视频名称

        return self.loadSteps(self.yaml_path, "getUpnextVideoName")

    def closeVideo(self):
        # 关闭视频
        self.swipe("down")
        if "Cancel" in self.driver.page_source:
            self.loadSteps(self.yaml_path, "clickCancel")
        self.loadSteps(self.yaml_path, "closeVideo")


