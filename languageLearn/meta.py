#创建列表
#[]就是空的列表
a=[]

#list创建列表
b=list()

#可以在创建列表的时候，指定初始值
c=[1,2,34,5]
print(c)

#可以在列表中，放不同类型的参数
d=[1,2,"sdad",True,[1,2,3,4]]
print(d)

#通过下标访问操作进行访问对应的元素
#这里的下标和c语言一样
d[1]=100
print(d[3])
#可以计算d中有多少个元素
print(len(d))

#[-1]代表最大的下标
print(d[-1])





#切片操作:代表的列表的一段区间，左闭右开
print(d[1:3])

# 取到完
print(d[1:])

#切片还可以指定步长
#每隔1个元素来取d中的一个元素
print(d[::1])

print(d[::2])

#遍历
for elem in d:
    print(elem)

#下标遍历
for i in range(0,len(d)):
    print(d[i])


d.append('hello')
d.append(12)
#往下标为1的位置插入元素
d.insert(1,1)
i=0
while i<len(d):
    print(d[i])
    i+=1


#判断元素是否在列表中存在
# in 
print(2 not in d)
print(1 in d)

# 使用index获得元素的下标
d.pop()
#删除下标为2的元素
d.pop(2)
print(d.index('hello'))
print(d.index(-1))
#使用remove
d.remove('hello')

#列表的拼接
m=[1,2]

new=m+d

k=[1,2]
# 把m拼接到k中

k.extend(m)
k+=m
