from bs4 import BeautifulSoup

#打开文件，把文件内容读取到html中
with open("./index.html") as f:
    html_doc=f.read()

#把文本放到解析器进行解析
soup=BeautifulSoup(html_doc,"html.parser")
#查找所有的div节点

links=soup.find_all("a")
#对里面的每个节点进行遍历

for link in links:
    print(link.name,link["href"],link.get_text())
