import os
import stat
#创建文件夹
def mkdir(path:str):
    #去除首位空格
    path=path.strip()
    #去除尾部空格
    path=path.rstrip("\\")
    #判断路径存在
    IsExists=os.path.exists(path)
    if not IsExists:
        #如果路径不存在，就创建目录
        #mkdir当父目录不存在的时候不会创建，而makedirs会创建多级目录
        
        #使用utf8解码
        os.makedirs(path.encode('utf-8'))
        print(f"{path} 创建成功")
        return True

    else:
        print(f"{path} 已经存在")
        return False

    
path="./ab/he.py"
#这个可以分隔路径前的所有的目录，和最后的文件名字

def getdirname(path):
    (directory,filename)=os.path.split(path)
    print(directory,filename)




mkdir(path=path)
filename='success.html'
str=path+'/'+filename
ttt='ab/file.py'
mode=0o600|stat.S_IRUSR
os.mknod(ttt,mode)
getdirname(path)