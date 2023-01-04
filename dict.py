#{}表示字典，构造一个字典
a={"id":1,"zhansan":"hello"}
d=dict()
print(a)

print("id" in a)
print(2 in a)
print(a["id"])
a[122]=123
a.pop(122)
for elem in a:
    print(elem,a[elem])

print(a.keys())
print(a.values())

for key,value in a.items():
    print(key,value)

#计算hash值:列表和字典是不可以hash的，可变的对象一般都是不可hash的
print(hash(12))
print(hash([1,23,4]))
print(hash((1,2,34,3)))
print(hash(a))