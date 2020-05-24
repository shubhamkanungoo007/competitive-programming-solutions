list1=[2,1,6]
list2=[1,5]
m=len(list1)
n=len(list2)
a=0
c=0
b=0
for i in range(m):
    for j in range(n):
        c=list1[i]**list2[j]
        b=list2[j]**list1[i]
        if c>b:
            a+=1
print(a)