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

    def login(self, var1, var2):
        # 登陆
        self.loadSteps(self.yaml_path, "login", account=var1, password=var2)
        return self

    def getUserName(self):
        # 获取登陆的账号名
        return self.loadSteps(self.yaml_path, "getUserName")

    def clickReply(self):
        # 点击小铃铛的第一层页面
        self.loadSteps(self.yaml_path, "clickReply")
        return self

    def clickComment(self):
        # 点击小铃铛的第二层页面
        try:
            self.loadSteps(self.yaml_path, "clickComment")
        except:
            try:
                self.loadSteps(self.yaml_path, "clickComment1")
            except:
                try:
                    self.loadSteps(self.yaml_path, "clickComment2")
                except:
                    print("没找到合适执行用例的二级评论")
        return self

    def reply(self,var1):
        # 回复评论
        self.loadSteps(self.yaml_path, "reply", keyword=var1)
        return self

    def delReply(self):
        # 删除评论
        self.loadSteps(self.yaml_path, "delReply")
        return self

    def clickVideo(self):
        # 点击视频
        self.loadSteps(self.yaml_path, "clickVideo")
        return self


    def changeChannel(self, var1):
        # 查看是否有debug入口
        debug = self.loadSteps(self.yaml_path, "isDebug")
        if debug == None:
            # 打开debug入口
            self.loadSteps(self.yaml_path, "openDebug")
        debugMode = self.loadSteps(self.yaml_path, "isDebugMode")
        if debugMode == '0':
            # 打开debug模式
            self.loadSteps(self.yaml_path, "openDebugMode")
        self.loadSteps(self.yaml_path, "changeChannel", channel=var1)
        return self

    def clickVip(self):
        # Me页面入口
        self.loadSteps(self.yaml_path, "clickVip")
        return self

    def clickContinue(self):
        # VIP页面点击continue
        self.loadSteps(self.yaml_path, "clickContinue")
        return self

    def CancelPay(self):
        # 取消支付
        self.loadSteps(self.yaml_path, "CancelPay")
        return self

    def clickTerms(self):
        # 查看terms协议
        self.loadSteps(self.yaml_path, "clickTerms")
        return self

    def clickEULA(self):
        # 查看EULA协议
        self.loadSteps(self.yaml_path, "clickEULA")
        return self

    def clickRestore(self):
        # 点击restore
        self.loadSteps(self.yaml_path, "clickRestore")
        return self