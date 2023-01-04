from crawl import url_manager

a='http://www.crazyant.net/'
urls=url_manager.urlManager()
urls.add_NewUrl(a)
c=urls.geturl()
str="http://www.crazyant.net/3002.html"
urls.add_NewUrl(str)