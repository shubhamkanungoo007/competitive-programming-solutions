a=int(input())
list=[]
for j in range(a):
    b=int(input())
    list.append(b)
print(list)
n=len(list)
list.sort()
ma=max(list)
mi=min(list)
for i in range(mi,ma):
    if i in list:
        pass
    else:
        print(i)
    
