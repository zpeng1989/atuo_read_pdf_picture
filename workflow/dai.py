# encoding: utf-8
import time
import sys
time1 = time.time()
import urllib, urllib2, base64
import json
import re



def get_token(API_Key,Secret_Key):
    # 获取access_token
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+API_Key+'&client_secret='+Secret_Key
    print(host)
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)#.decode()
    content = response.read()
    content_json=json.loads(content)
    access_token=content_json['access_token']
    return access_token


def recognition_word_high(filepath,filename,access_token):
    url='https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + access_token
    # 二进制方式打开图文件
    f = open(filepath + filename, 'rb')  # 二进制方式打开图文件
    # 参数image：图像base64编码
    img = base64.b64encode(f.read())
    params = {"image": img}
    params = urllib.urlencode(params)
    request = urllib2.Request(url, params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        with open('output_file_one.txt','w') as output_data:
            world=re.findall('"words": "(.*?)"}',str(content),re.S)
            for each in world:
                print(each)
                each_in = each + '\n'
                output_data.write(each_in)

def run_app(filepath,filename):

    access_token=get_token(API_key,Secret_Key)
    recognition_word_high=recognition_word_high(filepath,filename,access_token)


if __name__ == '__main__':
    API_Key = ""
    Secret_Key = ""
    filepath = ""
    filename=""
    access_token=get_token(API_Key,Secret_Key)
    recognition_word_high=recognition_word_high(filepath,filename,access_token)



