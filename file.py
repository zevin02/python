# 
f=open("qrcode.png",'r')
print(f)
#关闭文件
f.close()
#打开文件的
f=open("raw.txt",'w')
f.write("hello")
f.write('111')
print(f)
f.close()

f=open("raw.txt",'r',encoding='utf8')
#read(n):n 是要读取多少个字符
#没有参数就是读取所有的字符
result=f.read()
print(result)
lists=f.readlines()
print(lists)
#按行读取文件的所有元素

for line in f:
    print(line)


#上下文管理器
def func():
    #with会自动管理关闭文件f
    with open("raw.txt","r") as f:
        
