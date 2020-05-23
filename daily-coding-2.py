list=[3,2,1]
n=len(list)
left=[0]*n
right=[0]*n
left[0]=1
right[n-1]=1
pro=[0]*n
print("RIGT: ",right)
# print("left :",left[n-1])
# print("arr :",list[i-1])
for i in range(1,n):
    left[i]=list[i-1] + left[i-1]
    print("LIST[i-1] ",list[i-1]," LEFT[i-1]",left[i-1])
    print(left[i])
for j in range(n-2,-1,-1):
    print("THis j ",j)
    print("rigth: ",right[j+1])
    print("list :", list[j+1])
    right[j] = list[j + 1] + right[j + 1]
    print(right[i])
for i in range(n):
    pro[i]=left[i]+right[i]
#for i in range(n):
print(pro)
print(left)
print(right)
