def add(beg,end):
    thesum=0
    for i in range(beg,end):
        thesum+=i
    print(thesum)
    return thesum

#1-100的和
a=add(1,100)
add(2,33)
print(f"a={a}")

def test():
    print("add")
    print("hh")

test()

#判断是否为奇数
def isOdd(num):
    if num%2==0:
        return False
    else:
        return True

print(isOdd(123))

def getindex():
    x=10
    y=21
    return x,y#可以返回多个返回值

#使用多元赋值的方法来进行操作
a,b=getindex()


#只有函数和类有作用域影响
#而其他像for while if elif 这些都不会有影响


def fab(n):
    if n==1:
        return 1
    return fab(n-1)*n

def sum(x,y,debug=False):
    if debug:
        print(f"x={x},y={y}")
    return x+y

sum(1,2,True)


#按照形式参数的名字进行传参数,明显的告诉我这个参数要传给谁
s=sum(x=1,y=2)
print(s)
