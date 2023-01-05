#倒入datetime模块起别名为dt
import datetime as dt
# 从datetime模块中倒入datetime类型
from datetime import datetime
import requests

import datetime


date1=datetime.datetime(year=2022,month=1,day=14)
date2=datetime.datetime(year=2022,month=3,day=24)

print(date2-date1)

def reverse(str):
    begin=0
    end=len(str)-1
    while begin<=end:
        str[begin],str[end]=str[end],str[begin]
        begin+=1
        end-=1
    
    return str

str=reverse(['h','e','l','l','o',' ','w','o','r','l','d'])
print(str)

