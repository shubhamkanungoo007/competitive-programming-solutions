n=int(input())
for i in range(n):
    count=0
    b=input()
    c=list(b)
    for j in range(len(b)-1):
        if c[j]==0 and c[j+1]==1 and c[j+2]==0:
            count+=1
    print(count)