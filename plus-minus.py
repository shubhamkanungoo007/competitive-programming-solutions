list=[-4, 3, -9, 0, 4, 1]
n=len(list)
print(n)
print(list)
pos=0
neg=0
z=0
for i in list:
    if i>0:
        pos+=1
    elif i < 0:
        neg+=1
    elif i==0:
        z+=1
print("Psoitive :",pos,"Negative :", neg ,"Zero :",z  )
re1=pos/n
re2=neg/n
re3=z/n
lis=[re1,re2,re3]
print(lis)
    

############################################################### Hacker Rank Vaild Code at Down   ##########################################
# n=int(input())
# list = list(map(int,input().split()))
# n=len(list)
# # print(n)
# # print(list)
# pos=0
# neg=0
# z=0
# for i in list:
#     if i>0:
#         pos+=1
#     elif i < 0:
#         neg+=1
#     elif i==0:
#         z+=1
# #print("Psoitive :",pos,"Negative :", neg ,"Zero :",z  )
# re1=pos/n
# re2=neg/n
# re3=z/n
# #lis=[re1,re2,re3]
# print('%.6f'%re1)
# print('%.6f'%re2)
# print('%.6f'%re3)
    