import json
import os
import time


def analayz():
    # 构建结束统计测试结果
    path = os.path.dirname(os.getcwd())
    print("构建结束统计测试结果")
    time.sleep(10) # 等待allure报告
    f = open("%s/report.json" % path, "r")
    file = json.load(f)
    print(file)
    result = ""
    summary = dict(file["summary"])
    passed = summary.get("passed", "0")
    failed = summary.get("failed", "0")
    error = summary.get("error", "0")
    total = summary.get("total", "0")
    result = result.join("PASSED=%s\nFAILED=%s\nERROR=%s\nTOTAL=%s\n" % (passed,failed,error,total))
    file = open("%s/report.json" % path, "w")
    file.write(result)
    print(result)
    f.close()
    file.close()


if __name__ == '__main__':
    analayz()