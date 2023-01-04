#1.指定url
#2.下载内容
#3.提取数据

import requests
url="https://blog.csdn.net/m0_61567378?spm=1000.2115.3001.5343"
#获得网页数据,下载下来
r=requests.get(url)

#状态码不是200时就抛异常
if r.status_code!=200:
    raise Exception()

#获得文本内容
html_doc=r.text
from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,"html.parser")

#先查找h2标签节点
h2_nodes=soup.find_all("article",class_="blog-list-box")
for node in h2_nodes:
    #再在这个节点中查找a超链接节点
    link=node.find("a")
    print(link["href"])
    title=node.find("h4")
    print(title.get_text())

print("ok")