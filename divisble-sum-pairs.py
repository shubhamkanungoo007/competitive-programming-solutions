ar=[1,3,2,6,1,2]
c=0
for i in range(len(ar)):
    for j in range(i,len(ar)-1):
        sum=ar[i]+ar[j+1]
        if sum%3==0:
            c+=1
print(c)
