#!/usr/bin/env python
# encoding=utf-8
# author = ‘Rakey’ 

import os,random,requests, re,time,json,urllib.request,datetime
from bs4 import BeautifulSoup

# 1.Requests得到html源码
def getHTML(url):
    # 给头文件伪装成浏览器访问
    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
        "Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/ 537.36 (KHTML,like Gecko) Chrome/68.0.3440.106 Safari / 537.36"]

    Current_header='User-Agent:'+ random.choice(my_headers)
    headers = {
        'User-Agent': Current_header,
        'Referer':'http://music.163.com',
        'Host':'music.163.com'
        }
    proxies= {'http':'http://61.135.155.82:443'}
    #处理url异常，返回网页源代码
    try:
        req = requests.get(url,headers=headers,proxies=proxies,timeout=10)
        req.encoding = req.apparent_encoding  #使用网页自带的编码输出转换
        # print('获取网页数据%s'%req)
        return req
    except requests.RequestException:
        print("Can't reach website：%s"%url)

#2.获取重定向网址
def getRedirectUrl(url):
    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
        "Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/ 537.36 (KHTML,like Gecko) Chrome/68.0.3440.106 Safari / 537.36"]

    Current_header = 'User-Agent:' + random.choice(my_headers)
    headers = {
        'User-Agent': Current_header,
        'Referer': 'http://music.163.com',
    }

    result1 = requests.get(url=songurl, headers=headers, verify=False, allow_redirects=False,timeout=10)
    result = result1.content
    new_requests_url = result1.headers['location']
    print('歌曲下载网址为：' + new_requests_url)
    return (new_requests_url)

# 3.BS4得到一个bs4_url对象
def creatSoup(url):
    i = 1
    html_text = getHTML(url)
    #如果是异常网址，抛出错误
    while True:
        if html_text is None:
            print("url fail！")
            print('正在第%d次努力重试' % i)
            html_text = getHTML(url)
            i=i+1
            time.sleep(1)
        else:
            html_text = getHTML(url).text
            soup_0 = BeautifulSoup(html_text, 'html.parser')
            return soup_0

#4.写入TXT文本
def writeTxt(filename,content):
    with open(filename, 'a',encoding='utf-8') as file_to_write:
        file_to_write.write(content)
        print('写入完毕，文件保存路径：%s，请查看' % filename)

#5.下载音乐
def download(songurl, musicpath):
    print('正在下载歌曲：')
    urllib.request.urlretrieve(songurl, musicpath, cbk)

#6.显示音乐下载进度
def cbk(a,b,c):
    '''''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    print('%.2f%%' % per,end=' ')

##############################主程序####################################
start = time.perf_counter()  #时间开始
##############################替换不适合的名字##########################
def rUnsupportChar(s):  # 替换不能作为目录名的字符 <> : * " ? |
    unSupChar = r'''
    <>:*"?\
    '''
    supChar=r'''
    ()-^~$-
    '''
    trans=str.maketrans(unSupChar,supChar)
    s = s.translate(trans)
    return s
###################参数设置区###########################################
#需要下载的歌曲ID
# sid='526116053'
# sid='1311347412'
#需要下载的歌曲网址
musicurl='https://music.163.com/discover/toplist?id='
id='19723756'
##############################获取歌曲id列表####################################
soup=creatSoup(musicurl+id)
category=soup.find('a',attrs={'class':'s-fc0','href':re.compile('{}'.format(id))}).get_text()
Title=soup.find("textarea").get_text()
song_json=json.loads(Title)
songid_list=[]
for detail in song_json:
    songid=str(detail['id'])
    songname=detail['name']
    songid_list.append(songid)
# 定义要存储音乐的路径
path = 'D:\\14 音乐\\{}'.format(category+'_'+str(datetime.datetime.now()).split(" ")[0].replace('-',''))
###################创建文件夹###########################################
if os.path.exists(path):
    print(path + 'is created')
else:
    os.makedirs(path)
    print('已为您创建目录：%s' % path)
for sid in songid_list:
    print(sid)
    # ##############################获取歌名####################################
    musicurl='https://music.163.com/song?id='+sid
    soup=creatSoup(musicurl)
    Title=soup.find("title").get_text()
    info_Org=Title.split('-')
    info=[]
    for info1 in info_Org:
        if ' ' in info1:
            info.append(info1.strip(' ').replace('/','_').replace(':',''))
    singerName,songName=info[0:2]
    #############################下载歌词####################################
    lyricurl = 'https://music.163.com/api/song/lyric?'+'id='+sid+'&lv=1&kv=1&tv=-1'  #歌词地址
    print('歌词网址为：%s' %(lyricurl))
    soup=creatSoup(lyricurl)
    data = soup.get_text('lrc')
    contents = json.loads(data)
    if (contents.get('nolyric') or contents.get('uncollected')):
        print('没有歌词')
    else:
        lyric_Org=contents['lrc'].get('lyric').split('\n')
        regex = re.compile(r'\[.*\]')
        lyric=[]
        for i in range(len(lyric_Org)):
            if '[0' in lyric_Org[i]:
                lyric.append(re.sub(regex, '', lyric_Org[i].strip()))
            else:
                lyric.append(lyric_Org[i][(lyric_Org[i].find(':')+1):(len(lyric_Org[i])-1)])
        lyric_New=singerName+'--'+songName+'\n'+'\n'.join(lyric)
        print(lyric_New)
    ###################通过歌手名及歌曲名确定参数，并写入文本###########################################
    str=rUnsupportChar(singerName)+'-'+rUnsupportChar(songName)
    lyricName =str +'.txt'
    lyricPath=path+'\\'+lyricName
    writeTxt(lyricPath,lyric_New)
    ##############################下载歌曲####################################
    songurl='http://music.163.com/song/media/outer/url?id='+sid+'.mp3'
    musicpath = path+'\\'+str+'.mp3'
    print('准备下载歌曲，路径为：%s'%musicpath)
    songurl_New=getRedirectUrl(songurl)
    download(songurl_New,musicpath)
    print('音乐下载完毕，保存在：%s'%musicpath)
    end = time.perf_counter()  ##时间结束
    total_time = end - start
    print('写入完毕，歌词歌曲保存路径：%s,%s，请查看'%(lyricPath,musicpath))
    print("总耗时:%s秒,平均单曲下载时间为%f秒" %(total_time,total_time))