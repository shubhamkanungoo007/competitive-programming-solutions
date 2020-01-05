ls=[2,3,4,5,6,7,9,9,7,7]
ls1=[]
for i in ls:
    if i not in ls1:
        ls1.append(i)
print(ls1)