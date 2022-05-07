from Page.BasePage import BasePage
from Page.MainPage import MainPage


class App(BasePage):

    @classmethod
    def main(cls):
        cls.getClient().restartApp()
        return MainPage()