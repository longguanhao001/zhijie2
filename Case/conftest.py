#  encoding: utf-8
import sys
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")

from Driver.ClientDriver import ClientDriver

import os
import shutil

import pytest
from _pytest import terminal
from Page.App import App


@pytest.fixture(scope="session", autouse=True)
def cleanScreenShot():
    #  清理screenShot文件夹
    shutil.rmtree("../ScreenShot")
    os.mkdir("../ScreenShot")
    #  安装app
    App.maininstall()

    yield
    # #  清理Package文件夹
    # shutil.rmtree("../Package")
    # os.mkdir("../Package")
    driver = ClientDriver.driver
    driver.quit()
