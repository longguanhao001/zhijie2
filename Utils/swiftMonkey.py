import base64
import hashlib
import hmac
import os
import re
import time
import urllib

import requests
from tinydb import TinyDB, Query


def _getSign(secret):
    '''
    根据秘钥获取时间戳和签名
    :param secret: 秘钥地址
    :return: 时间戳、签名
    '''
    timestamp = round(time.time() * 1000)
    timestamp = str(timestamp)
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign

def dingding_bysign(data, assess_token, secret):
    '''
    发送钉钉消息
    :param data:发送消息的消息体
    :param assess_token: web_hook的token，并不是一长串的url，只需要里面的access_token
    :param secret: 勾选加签生成的字符串
    :return: 发送到钉钉返回的响应
    '''
    timestamp, sign = _getSign(secret)
    dingding_robot_token = "https://oapi.dingtalk.com/robot/send?access_token={assess_token}&&timestamp={timestamp}&sign={sign}".format(
        timestamp=timestamp, sign=sign, assess_token=assess_token)
    headers = {'content-type': 'application/json'}
    r = requests.post(dingding_robot_token, headers=headers, data=json.dumps(data))
    r.encoding = 'utf-8'
    print(r.text)
    return r.text

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
            report = open("%s/%s" % (path, f), "r")
            data = report.read()
            report_time = re.findall(r'Time:(.*?)\.', data)[0]
            report_time = str(report_time).replace(" ", "")
            version = re.findall(r'Version:(.*?)\(', data)[0]
            version = str(version).replace(" ", "")
            OS_version = re.findall(r'OS Version:(.*?)\n', data)[0]
            OS_version = str(OS_version).replace(" ", "")
            print("%s,%s,%s" % (report_time, version, OS_version))
            # 测试群
            token = "8f67c89ef25c3d9b7b0555538369c09cdcfc5eac9dfec4dfe6d3614b05cd689c"
            secret = "SEC5a50a1f460a7f7f32326480630c6c88391b26310372974c478c6ac24dfa19af5"
            # 正式群
            # oken = "c8ff7a0774d36dfa02e33bfad99b36570e984e195e69437c942560961f6ade4b"
            # secret = "SEC658edeb2de8017fb2b7c6bc1065b8683dcfa44ac78929506e9b814733329b339"
            dingdata = {'msgtype': 'markdown',
                        'markdown': {'title': 'Monkey Test for ' + version, 'text': '1 Carsh&ANR\nreportTime:%s\ntestDevices:%s\n请在bugly平台处理https://bugly.qq.com/v2/crash-reporting/crashes/335c93a88a?pid=2'%(report_time, OS_version)},
                        # 'at': {"atMobiles": ["13524352709"], "isAtAll": False}}
                        }
            dingding_bysign(dingdata, token, secret)
            print("上报dingding和bug")

        else:
            print("今天已经上报过该崩溃")

    # 记录截图
