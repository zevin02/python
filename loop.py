num=1
sum=0;
while num<=10:
    print(num)
    sum+=num
    num+=1

print(f"sum={sum}")

total=1
n=1
while n<=5:
    total*=n
    n+=1
print(total)

#打印1-10
for i in range(1,11):
    print(i)

# range还提供了步长
# 1,3,5,7;i+=2
for i in range(1,11,2):
    print(i)

sum=0
for i in range(1,101):
    sum+=i
    if i==5:
        continue
    if i==13:
        break
print(sum)

thesum=0
cout=0
while cout<4:
    cout+=1
    a=int(input())
    thesum+=a
thesum/=4
print(thesum)
