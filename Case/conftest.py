#  encoding: utf-8
import sys

sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")

from Driver.ClientDriver import ClientDriver

import os
import shutil

import pytest
from Page.App import App


@pytest.fixture(scope="session", autouse=True)
def cleanScreenShot():
    #  清理screenShot文件夹
    shutil.rmtree("../ScreenShot")
    os.mkdir("../ScreenShot")
    #  安装app
    App.maininstall()

    yield
    driver = ClientDriver.driver
    driver.quit()
