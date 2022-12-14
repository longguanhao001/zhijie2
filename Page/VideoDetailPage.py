import time

from Page.BasePage import BasePage


class VideoDetailPage(BasePage):
    yaml_path = "../Data/$channel/VideoDetailPage.yaml"

    def LoginPageBack(self):
        # 跳转到登陆页后返回
        self.loadSteps(self.yaml_path, "LoginPageBack")

    def clickVideo(self):
        # 点击视频画面
        self.loadSteps(self.yaml_path, "clickVideo")
        return self

    def get_nowProgress(self):
        # 获取当前视频进度
        return self.loadSteps(self.yaml_path, "get_nowProgress")

    def get_nowProgress1(self):
        # 获取当前视频进度
        m, s = self.loadSteps(self.yaml_path, "get_nowProgress").split(':')
        now_progress = int(m)*60+int(s)
        time.sleep(3)
        m, s = self.loadSteps(self.yaml_path, "get_allProgress").split('/')[1].split(':')
        all_progress = int(m)*60+int(s)
        return int(now_progress/all_progress*10)

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
        if self.is_exits("SUBSCRIBE"):
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

    def closeRestrited(self):
        # 关闭限制模式
        return self.loadSteps(self.yaml_path, "closeRestrited")

    def sendComment(self, var1):
        # 发送评论
        return self.loadSteps(self.yaml_path, "sendComment", keyword=var1)

    def deleteComment(self):
        # 删除评论
        return self.loadSteps(self.yaml_path, "deleteComment")


