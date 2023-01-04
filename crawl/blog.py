#倒入我们写的文件
import url_manager
import requests
from bs4 import BeautifulSoup
import re

#我们要判断url是否合理，所以要用正则表达时来进行判断处理

# url1="http://www.c.net/123.html"
# ^ 字符串起始位置，$字符串结尾，\d匹配数字,+表示数字可以很大
# pattern=r'^http://www.c.net/\d+.html$'





#要爬取网页的根地址
root_url="http://www.crazyant.net/"

#获得一个url管理器
urls=url_manager.urlManager()
urls.add_NewUrl(root_url)

#以写入模式打开一个文件 
fout=open("craw_all_page","w")
while urls.hasnewurl():
    print("hello")
    cururl=urls.geturl()
    #如果过了3秒还不返回就直接跳过，继续执行下面的操作 
    r=requests.get(cururl,timeout=3)
    if r.status_code!=200:
        print("error,return code is not 200",cururl)
        continue    

    soup=BeautifulSoup(r.text,"html.parser")
    #获得文本的标题
    title=soup.title.string
    #把文本的网址和标题写入文本中
    fout.write("%s\t%s\n"%(cururl,title))
    #刷盘
    fout.flush()
    print(f"success {cururl} {title}")
    # fout.write(f"{cururl}  {title}")
    #在这个下面查找所有的链接
    links=soup.find_all("a")
    for link in links:
        href=link.get("href")
        if href is None:
            continue
        
        pattern=r'^http://www.crazyant.net/\d+.html$'
        if re.match(pattern,href):
            #字符串匹配，就添加进去
            print(href)
            urls.add_NewUrl(href)
            
            print(urls.size())
            print("add")
    

print("ok")
fout.close()