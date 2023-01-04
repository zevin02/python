# 元组是只读的，不能修改元组的内容


#创建元组
a=()
print(type(a))
b=tuple()

a=(1,2,3,"hello",True,[331,2],(12,3))
print(a)
print(a[0])
print(a[-1])
for i in range(0,len(a)):
    print(a[i])

print(a[1:3])
for elem in a:
    print(elem)

print(3 in a)
print(a.index("hello"))

b=(2,3)
b+=a
