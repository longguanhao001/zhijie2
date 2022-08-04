import os

if __name__ == '__main__':
  	#执行monkey
    result = os.popen("xcodebuild -project /Users/vanced/Downloads/sjk_swiftmonkey/sjk-monkey.xcodeproj -scheme sjk-monkey -destination 'id=20a7adaffd52ebb0f01efea599592e4272297911' test")
    print(result)
    #记录日志
    #记录截图
    #扫描崩溃
    #上报dingding+提bug