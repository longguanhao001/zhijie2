import os
import shutil

import pytest

@pytest.fixture(scope="module", autouse=True)
def cleanScreenShot():
    #  清理screenShot文件夹
    shutil.rmtree("../ScreenShot")
    os.mkdir("../ScreenShot")
