list=[1,2,3,44,51,7]
mx=int(input())
mn=int(input())
l1=[]
# mx=50
# mn=55
for i in range(mx,mn+1):
    if i not in list:
        l1.append(i)
    else:
        #l1.append(i)
        pass
print(l1)

