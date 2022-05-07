from Page.BasePage import BasePage
from Page.MainPage import MainPage


class App(BasePage):

    @classmethod
    def main(cls):
        # 初始化应用
        cls.getClient().restartApp()
        return MainPage()