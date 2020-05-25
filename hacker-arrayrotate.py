list=[1,2,3,4,5]
n=2
le=len(list)
list1=[0,0]
list2=[0,0,]
for i in range(0,n):
    list1[i]=list[i]
    #list.remove(list[i])
for j in range(n,le):
    list2[j]=list[j]
print(list)
print(list2+list1)

