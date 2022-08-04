import os
import time

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
    # 上报dingding+提bug
    # 记录截图
