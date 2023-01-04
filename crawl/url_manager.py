class urlManager:
    # url管理器
    def __init__(self):
        #一个新的需要添加进去进行爬取的url集合
        #一个是已经爬取过的url的集合
        self.newurls=set()
        self.oldurls=set()
    
    
    
    def add_NewUrl(self,url):
        #如果这个url是一个空，或长度为0,就不应该添加进来
        if url is None or len(url)==0:
            return
        #如果这个url已经被处理过了，那么也不应该添加进来
        if url in self.newurls: 
            return
        if url in self.oldurls:
            return
        #添加到待处理的集合中
        self.newurls.add(url)


    def add_NewUrls(self,urls):
        #批量的添加urls
        if urls is None or len(urls)==0:
            return

        #批量的添加一个url
        for url in urls:
            self.add_NewUrl(url)
        
    


    def geturl(self):
        #获得一个url
        if self.hasnewurl():
            #获得一个url同时去除
            url=self.newurls.pop()
            #
            self.oldurls.add(url)
            return url
        else:
            return None


    def hasnewurl(self):
        return len(self.newurls)>0
    
    def size(self):
        return len(self.newurls)

if __name__=="__main__":
    url_magr=urlManager()
    url_magr.add_NewUrl("url1")
    url_magr.add_NewUrls(["url1","url2"])
    newurl=url_magr.geturl()
    print(newurl)
    print(url_magr.hasnewurl())