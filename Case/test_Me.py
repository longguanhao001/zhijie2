#  encoding: utf-8
import sys
import time

sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")

import allure

from Page.App import App
from Utils.Assert import Assert

@allure.feature("Me页测试用例")
class TestMe():

    @classmethod
    def setup_class(cls):
        # 执行用例前重启app
        cls.pureMain = App.main()

    @allure.story("未登录时点击小铃铛会跳转到登陆页")
    def test_bell_unlogin(self):
        MePage = self.pureMain.goto_Me()
        time.sleep(3)
        MePage.clickBell()
        time.sleep(3)
        Assert().assert_in("Email or phone", MePage.driver.page_source)




