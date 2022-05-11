from Page.BasePage import BasePage


class MePage(BasePage):
    yaml_path = "../Data/$channel/MePage.yaml"
    def clickSign_in(self):
        # 点击登陆
        self.loadSteps(self.yaml_path, "clickSign_in")

    def clickBell(self):
        # 点击小铃铛
        self.loadSteps(self.yaml_path, "clickBell")

    def clickSettings(self):
        # 跳转到设置页
        self.loadSteps(self.yaml_path, "clickSettings")

    def feedback(self):
        # 反馈功能
        self.loadSteps(self.yaml_path, "feedback")

    def privacy_policy(self):
        # 跳转到协议页
        self.loadSteps(self.yaml_path, "privacy_policy")

    def share_app(self):
        # 分享app
        self.loadSteps(self.yaml_path, "share_app")
