# -*- coding: utf-8 -*-
# Author：jin

import urllib,urllib2

def load_page(full_urlname,filename):
    headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
    request = urllib2.Request(full_urlname,headers = headers)
    response = urllib2.urlopen(request)
    files = response.read()
    print('正在下载'+filename)
    return files

def write_page(files,filename):
    with open('Tspider.txt','w') as fw:
        fw.write(files)
        print('正在保存' + filename)
        # print("-"*30)

def spider(urlname,begin_page,end_page):
    for i in range(begin_page,end_page+1):
        num = (i-1)*50
        full_urlname = urlname + '&pn='+str(num)
        filename = "第"+str(i) +"页"
        files = load_page(full_urlname,filename)
        write_page(files,filename)
        print(full_urlname)
        print("-"*30)

if __name__ == '__main__':
    url = "http://tieba.baidu.com/f?"
    k = raw_input("请输入贴吧名：")
    kw = urllib.urlencode({'kw': k})
    # print(kw)
    begin_page = int(raw_input("请输入起始页面："))
    end_page = int(raw_input("请输入结束页面："))
    urlname = url + kw
    spider(urlname, begin_page, end_page)





