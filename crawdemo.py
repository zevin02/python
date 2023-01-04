import requests
from bs4 import BeautifulSoup
import selenium


#requests 常常可以用于爬虫中对网页内容的下载

print('ok')
url="http://www.crazyant.net"
r=requests.get(url)
r.status_code