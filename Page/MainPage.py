from Page.BasePage import BasePage
from Page.SearchPage import SearchPage


class MainPage(BasePage):

    def goto_Me(self):
        # 跳转到me页
        pass

    def goto_Search(self, var1):
        # 跳转到me页
        self.loadSteps("../Data/$channel/MainPage.yaml", "goto_Search", keyword=var1)
        return SearchPage()