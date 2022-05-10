import sys
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest/venv/lib/python3.8/site-packages")
sys.path.append(r"/Users/huangzhijie/PycharmProjects/PureIosAutoTest")
import os
import shutil

import pytest

from Page.App import App


@pytest.fixture(scope="module", autouse=True)
def cleanScreenShot():
    #  清理screenShot文件夹
    shutil.rmtree("../ScreenShot")
    os.mkdir("../ScreenShot")
    #  安装app
    App.maininstall()

    yield
    #  清理Package文件夹
    shutil.rmtree("../Package")
    os.mkdir("../Package")
