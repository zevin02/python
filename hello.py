print(1+2-3)
print(2*3-4)
print(1+3/5)
print((67.5+89.8+12.9+32.4)/4)
avg = (67.5+89.0+12.5+65)/4     # 添加一个变量
total = (66-avg)**2+(89.5+avg)**2   # **代表乘方
ret = total-avg
print(ret)

a = 13
a1 = 14
A = 13
A += 3
a2 = A
# if=12   # 关键字不能做变量

print(A)
a = 66
print(type(a))
b = 0.2
print(type(b))

e = 'asdsdsd"asd"'
h = 'sds'  # '和"都可以

print(e)
size = len(e)  # 计算字符串长度
print(size)
print(len("aaaaa"))
str = "asdd"
sss = "fff"
ccc = str+sss
print(ccc)
print("sd"+"cd")
c1 = True
c2 = False
print(c1)
a = 12
a = "sd"
print(a)
# python 是动态类型，类新可以变化类型
x = 13
# 格式化输出a=13
print(f"a={x+133}")
num=input('请输入一个和数:')# 执行的时候就会等待用户进行输入
print(f"您输入的数字是{num}")

a=input('在输入一个数')
b=input('在输入二个数')
c=input('在输入3个数')
d=input('在输入4个数')
a=int(a)    #把a从str类型变成int
b=int(b)
c=int(c)
d=int(d)
num=(a+b+c+d)/4
print(f"num={num}")
print(f"a+b={a+b}")
# a=str(a)
# a=float(a)

# **是乘方运算
print(4**3)

# //向下取整数
# 7/2向下取整数=3，往小的地方取
print(7//2)
print("dsa"=="dsa")
# 比较浮点数,看是否在误差范围内
b=0.1+0.3
a=0.1+0.3
print(-0.000001<(a-b)<0.000001)# 连续相等

print(1<2 and 2<3)
print(1<2 or 5<3)
print(not 1<3)# 逻辑取反
print(1<2<34)
a,b=10,30# 10=a,b=30,不推荐
a=10
b=20
a,b=b,a #交换两个数
print(a,b)

#python 不支持++，--


