import time

from Page.BasePage import BasePage


class MePage(BasePage):
    yaml_path = "../Data/$channel/MePage.yaml"
    def clickSign_in(self):
        # 点击登陆
        self.loadSteps(self.yaml_path, "clickSign_in")
        return self

    def clickBell(self):
        # 点击小铃铛
        self.loadSteps(self.yaml_path, "clickBell")

    def clickSettings(self):
        # 跳转到设置页
        self.loadSteps(self.yaml_path, "clickSettings")

    def feedback(self,var1):
        # 反馈功能
        self.loadSteps(self.yaml_path, "feedback",keyword=var1)

    def privacy_policy(self):
        # 跳转到协议页
        self.loadSteps(self.yaml_path, "privacy_policy")

    def share_app(self):
        # 分享app
        self.loadSteps(self.yaml_path, "share_app")
        # time.sleep(2)  ios该方法无效
        # pasteboard_text = self.driver.get_clipboard_text()
        # return pasteboard_text

    def clipboardValue(self):
        # 将剪切板的文字粘贴到输入框里
        self.loadSteps(self.yaml_path, "clipboardValue")

    def clickPolicy(self):
        # 跳转到policy页
        self.loadSteps(self.yaml_path, "clickPolicy")
        return self
