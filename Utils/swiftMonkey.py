import os
import time
from tinydb import TinyDB, Query

if __name__ == '__main__':
  	#   执行monkey
    # 记录日志
    # 扫描崩溃
    fileList = []
    path = "/Users/vanced/Downloads/crashreport"
    date_str = time.strftime('%m-%d', time.localtime())
    for root, dirs, files in os.walk(path, topdown=False):
        for f in files:
            if "PureTuber" in f and date_str in f:
                fileList.append(f)
    print(fileList)
    # 数据库检验bug是否存在，不存在的话就上报
    db = TinyDB("database.json")
    table = db.table("iOSMonkey")
    for f in fileList:
        # 创建一个用户查询对象
        User = Query()
        # 查询一个用户名为Sally的数据
        query_data = table.search(User.reportName == f)
        if len(query_data) < 1:
            # 上报dingding+提bug
            table.insert({"reportName": f})
            print("上报dingding和bug")

        else:
            print("今天已经上报过该崩溃")

    # 记录截图
