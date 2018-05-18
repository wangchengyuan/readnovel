import os
import re
import novelconfig
try:
    import requests
except:
    os.system('pip install requests')
    import requests


data = {}
chapterdata = []

headers = {
    'Host': 'www.biquge.com.tw',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Pragma': 'no-cache'
}


def crawlcontent(url):
    resp = requests.get(url,headers=headers,timeout=10)
    resp.encoding = 'gbk'
    page = resp.text
    ret = 'nbsp;&nbsp;&nbsp;&nbsp;(.*?)\<'
    recontent = re.findall(ret, page)
    return recontent


def crawlchater(url):
    resp = requests.get(url,headers=headers,timeout=10)
    resp.encoding = 'gbk'
    page = resp.text
    rex = 'href="(.*?)">第(.*?)章(.*?)\<'
    recontent = re.findall(rex, page)
    print("现在最新章节如下：")
    for rec in recontent:
        data[rec[1]] = (rec[0],rec[2]) #字典rec[1]为章节数,rec[0]为章节url,rec[2]为章节名
        chapterdata.append(rec[1])
    for chapterd in chapterdata[-10:]:
        print(chapterd, data[chapterd][1])

#def localrecord():


if __name__ == '__main__':
    url=novelconfig.novelurls['url1']
    tag = True
    crawlchater(url)
    while tag:
        chapter = input("输入你想看的章节：")
        if chapter == '':
            tag = False
        else:
            newurl = 'https://www.biquge.com.tw' + data[chapter][0]
            content=crawlcontent(newurl)
            for con in content:
                print(con)