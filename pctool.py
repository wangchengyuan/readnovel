import os
import re
try:
    import requests
except:
    os.system('pip install requests')
    import requests


data = {}
data2 = {}
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
    #print(page)
    ret = 'nbsp;&nbsp;&nbsp;&nbsp(.*?)\<'
    recontent = re.findall(ret, page)
    for rec in recontent:
        #rec
        print(rec.replace(';', ''))


def crawlchater(url):
    resp = requests.get(url,headers=headers,timeout=10)
    resp.encoding = 'gbk'
    page = resp.text
    # print(page)
    rex = 'href="(.*?)">第(.*?)章(.*?)\<'
    recontent = re.findall(rex, page)
    print("现在最新章节如下：")
    for rec in recontent:
        data[rec[1]] = rec[0]
        data2[rec[1]] = rec[2]
        chapterdata.append(rec[1])
    for chapterd in chapterdata[-10:]:
        print(chapterd, data2[chapterd])
    # print(chapterdata[-10:])


if __name__ == '__main__':
    # 注意在运行之前，先确保该文件的同路径下存在一个download的文件夹, 用于存放爬虫下载的图片
    url1 = 'http://www.biquge.com.tw/17_17319/'  # 天神诀
    url2 = 'http://www.biquge.com.tw/16_16379/'  # 至尊剑皇
    url3 = 'http://www.biquge.com.tw/16_16209/'  # 我是至尊
    url4 = 'http://www.biquge.com.tw/8_8568/'  # 伏天氏

    tag = True

    crawlchater(url2)
    while tag:
        chapter = input("输入你想看的章节：")
        if chapter == '':
            tag = False
        else:
            newurl = 'https://www.biquge.com.tw' + data[chapter]
            crawlcontent(newurl)