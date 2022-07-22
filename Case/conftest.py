#  encoding: utf-8
import sys

sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")

from Driver.ClientDriver import ClientDriver

import os
import shutil

import pytest
from Page.App import App

is_login = False

@pytest.fixture(scope="session", autouse=True)
def cleanScreenShot():
    path = os.path.dirname(os.getcwd())
    #  清理screenShot文件夹
    shutil.rmtree("%s/ScreenShot" % path)
    os.mkdir("%s/ScreenShot" % path)
    #  安装app
    App.maininstall()

    yield
    driver = ClientDriver.driver
    driver.quit()


def pytest_collection_modifyitems(items):
    # 自定义用例执行顺序
    unlogin = []
    login = []
    end = []
    for item in items:
        if "_login" in item.name:
            if item.name == "test_login":
                login.insert(0, item)
            else:
                login.append(item)
        elif "_end" in item.name:
            end.append(item)
        else:
            unlogin.append(item)
    caselist = unlogin+login+end
    items.clear()
    for cases in caselist:
        items.append(cases)


