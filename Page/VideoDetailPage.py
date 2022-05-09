from Page.BasePage import BasePage


class VideoDetailPage(BasePage):

    def LoginPageBack(self):
        # 跳转到登陆页后返回
        self.loadSteps("../Data/$channel/VideoDetailPage.yaml", "LoginPageBack")

    def get_nowProgress(self):
        # 获取当前视频进度
        return self.loadSteps("../Data/$channel/VideoDetailPage.yaml", "get_nowProgress")

    def like(self):
        # 点击点赞按钮
        self.loadSteps("../Data/$channel/VideoDetailPage.yaml", "like")

    def dislike(self):
        # 点击点赞按钮
        self.loadSteps("../Data/$channel/VideoDetailPage.yaml", "dislike")

    def add_to(self):
        # 点击点赞按钮
        self.loadSteps("../Data/$channel/VideoDetailPage.yaml", "add_to")

    def backGroundPlay(self):
        pass

    def popupPlay(self):
        # 点击点赞按钮
        self.loadSteps("../Data/$channel/VideoDetailPage.yaml", "subsribe")

    def Share(self):
        pass

    def subsribe(self):
        # 点击点赞按钮
        self.loadSteps("../Data/$channel/VideoDetailPage.yaml", "subsribe")

    def open_comment(self):
        pass

    def clickUpnext(self):
        # 点击点赞按钮
        self.loadSteps("../Data/$channel/VideoDetailPage.yaml", "clickUpnext")

    def getLikeCount(self):
        # 获取点赞数量
        self.loadSteps("../Data/$channel/VideoDetailPage.yaml", "getLikeCount")

    def getUpnextVideoName(self):
        # 获取upnext视频名称
        self.loadSteps("../Data/$channel/VideoDetailPage.yaml", "getUpnextVideoName")