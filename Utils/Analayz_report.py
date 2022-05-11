import json
import time


def analayz():
    # 构建结束统计测试结果
    print("构建结束统计测试结果")
    time.sleep(10) # 等待allure报告
    f = open("../report.json", "r")
    file = json.load(f)
    result = ""
    summary = dict(file["summary"])
    passed = summary.get("passed", "0")
    failed = summary.get("failed", "0")
    error = summary.get("error", "0")
    total = summary.get("total", "0")
    result = result.join("PASSED=%s\nFAILED=%s\nERROR=%s\nTOTAL=%s\n" % (passed,failed,error,total))
    file = open("../report.txt", "w")
    file.write(result)
    print(result)
    f.close()
    file.close()


if __name__ == '__main__':
    analayz()