import base64
import hashlib
import hmac
import json
import os
import re
import time
import traceback
import urllib

import requests
from tinydb import TinyDB, Query
from jira import JIRA



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

def uploadFile(filepath):
    osslink = ''
    try:
        url = "http://161.117.69.170:81/upload_file"
        #url = 'http://172.21.2.150:8001/upload_file'
        fileparam = {'file': open(filepath, 'rb')}
        response = requests.post(url, files=fileparam)
        if response.status_code != 200:
            time.sleep(5)
            response = requests.post(url, files=fileparam)
        print(response.text)
        Data = json.loads(response.text)
        osslink = Data['data']['oss_url']
    except Exception as e:
        print(str(e))
    return osslink

def CreateJiraBug(project,title,desc, oss_link, dsym,assignee='',fixedver='' ):
    # 上传dsym文件
    dsym_link = uploadFile(dsym)
    desc = desc + "\n\ndsym:%s\n\ncrash_Report:%s" % (dsym_link,oss_link)

    # 报bug
    try:
        print('Report bug: ' + desc)
        jira_server = 'http://47.242.115.120:8283'  # jira地址
        jira_username = 'Flat'  # 用户名
        jira_password = 'flat175246'  # 密码
        jira = JIRA(basic_auth=(jira_username, jira_password), options={'server': jira_server})

        if project and title:
            try:
                if '' == fixedver:
                    jira.create_issue(project=str(project), summary=str(title),
                                      description=str(desc),assignee={'name': assignee},
                                      priority={'name': "High"},
                                      issuetype={'name': 'BUG'})
                else:
                    jira.create_issue(project=str(project), summary=str(title),
                                      description=str(desc), assignee={'name': assignee},
                                      priority={'name': "High"}, fixVersions=[{'name': fixedver}],
                                      issuetype={'name': 'BUG'}, components=[{'name': 'Monkey'}])
                result = {'status': 1}
                print(result)
                return result
            except Exception as e:
                result = {'status': 0, 'error': str(traceback.format_exc())}
                print(result)
                return result
        else:
            result = {'status': 0, 'msg': 'no project or title'}
            print(result)
            return result
    except Exception as e:
        print(str(e))

def installIpa():
    # install apk
    result = os.popen("/opt/homebrew/bin/ideviceinstaller  -u 00008020-000248693468002E -l").read()
    print(result)
    path = os.path.dirname(os.getcwd())
    file_name_list = os.listdir("%s/Package" % path)
    file_name = ""
    dsym = ""
    for i in file_name_list:
        if "ipa" in i:
            file_name = i
        else:
            dsym = i
    dsym = "%s/Package/%s" % (path,dsym)
    print(dsym)
    cur_path = os.path.dirname(os.getcwd())
    package_path = "%s/Package/%s" % (cur_path, file_name)
    if "video.test.tools.os" not in result:
        result = os.popen(
            "/opt/homebrew/bin/ideviceinstaller -u 00008020-000248693468002E -i '%s'" % package_path).read()
        print(result)
        os.remove(r"%s" % package_path)
    else:
        os.popen(
            "/opt/homebrew/bin/ideviceinstaller -u 00008020-000248693468002E -U 'video.test.tools.os'").read()
        result = os.popen(
            "/opt/homebrew/bin/ideviceinstaller -u 00008020-000248693468002E -i '%s'" % package_path).read()
        print(result)
        os.remove(r"%s" % package_path)
    return file_name, dsym


if __name__ == '__main__':
    file_name, dsym = installIpa()
    time.sleep(10)
  	# 执行monkey
    os.system("/usr/bin/xcodebuild -project /Users/vanced/Downloads/sjk_swiftmonkey/sjk-monkey.xcodeproj -scheme sjk-monkey -destination 'id=00008020-000248693468002E' test")

    # result = os.popen(
    #             "/usr/bin/xcodebuild -project /Users/vanced/Downloads/sjk_swiftmonkey/sjk-monkey.xcodeproj -scheme sjk-monkey -destination 'id=00008020-000248693468002E' test").read()
    # print(result)
    result = os.popen(
            "/opt/homebrew/bin/idevicecrashreport -u 00008020-000248693468002E -e -k /Users/vanced/Downloads/crashreport").read()
    # print(result)
    # 记录日志
    # 扫描崩溃
    fileList = []
    path = "/Users/vanced/Downloads/crashreport"
    date_str = time.strftime('%m-%d', time.localtime())
    for root, dirs, files in os.walk(path, topdown=False):
        for f in files:
            if "PureTuber" in f and date_str in f and "wakeups_" not in f:
                fileList.append(f)
    print(fileList)

    # 数据库检验bug是否存在，不存在的话就上报
    db = TinyDB("database.json")
    table = db.table("iOSMonkey")
    # 记录今天未上报的crash数量
    num = 0
    text = ""
    oss_link = []
    for f in fileList:
        # 创建一个用户查询对象
        User = Query()
        # 根据报告名查数据
        query_data = table.search(User.reportName == f)
        if len(query_data) < 1:
            # 上传crash报告
            oss_link.append(uploadFile("%s/%s" % (path, f)))
            # 上报dingding+提bug
            table.insert({"reportName": f})
            report = open("%s/%s" % (path, f), "r")
            data = report.read()
            report_time = re.findall(r'/Time:(.*?)\.', data)[0]
            report_time = str(report_time).replace(" ", "")
            version = re.findall(r'Version:(.*?)\(', data)[0]
            version = str(version).replace(" ", "")
            OS_version = re.findall(r'OS Version:(.*?)\n', data)[0]
            OS_version = str(OS_version).replace(" ", "")
            print("%s,%s,%s" % (report_time, version, OS_version))
            print("上报dingding和bug")
            num += 1
            text += '<font color=#A0522D>' + report_time + '</font>,<font color=#A0522D>' + OS_version + '</font>\n\n'

        else:
            print("今天已经上报过该崩溃")
    if text:
        text= "#### <font color=#228B22>Monkey Test for %s</font>\n\n**iPhone Xs,iOS14.8.1,00008020-000248693468002E**Carsh&ANR\n\n<font color=#A0522D>%s</font> Carsh&ANR\n\n%s请在bugly平台处理https://bugly.qq.com/v2/crash-reporting/crashes/335c93a88a?pid=2" % (file_name, num,text)
        # 测试群
        token = "8f67c89ef25c3d9b7b0555538369c09cdcfc5eac9dfec4dfe6d3614b05cd689c"
        secret = "SEC5a50a1f460a7f7f32326480630c6c88391b26310372974c478c6ac24dfa19af5"
        # 正式群
        # 正式群
        token = "c8ff7a0774d36dfa02e33bfad99b36570e984e195e69437c942560961f6ade4b"
        secret = "SEC658edeb2de8017fb2b7c6bc1065b8683dcfa44ac78929506e9b814733329b339"
        dingdata = {'msgtype': 'markdown',
                    'markdown': {'title': 'Monkey Test for ' + version,
                                 'text': text},
                    # 'at': {"atMobiles": ["13524352709"], "isAtAll": False}}
                    }
        dingding_bysign(dingdata, token, secret)
        # CreateJiraBug(project, title, desc, assignee='', fixedver=''):
        #创建jira bug
        CreateJiraBug("PTI", "%s%s Crash,test for monkey" % (version, num), text ,oss_link, dsym)
    else:

        text = "#### <font color=#228B22>Monkey Test for %s</font>\n\n**iPhone Xs,iOS14.8.1,00008020-000248693468002E**\n\n<font color=#A0522D>0</font> Carsh&ANR\n\n" % file_name
        # 测试群
        token = "8f67c89ef25c3d9b7b0555538369c09cdcfc5eac9dfec4dfe6d3614b05cd689c"
        secret = "SEC5a50a1f460a7f7f32326480630c6c88391b26310372974c478c6ac24dfa19af5"
        # 正式群
        token = "c8ff7a0774d36dfa02e33bfad99b36570e984e195e69437c942560961f6ade4b"
        secret = "SEC658edeb2de8017fb2b7c6bc1065b8683dcfa44ac78929506e9b814733329b339"
        dingdata = {'msgtype': 'markdown',
                    'markdown': {'title': 'Monkey Test for  + version',
                                 'text': text},
                    # 'at': {"atMobiles": ["13524352709"], "isAtAll": False}}
                    }
        dingding_bysign(dingdata, token, secret)
    # 记录截图
