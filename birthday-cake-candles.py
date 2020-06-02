list=[2,4,3,4,4]
count=0
a=max(list)
print(a)
for i in list:
    if i==a:
        count+=1
    else:
        pass
print(count)