b=0
arr=[1,4,4,4,5,3]
# list=[]
# for i in range(len(arr)):
#     b=arr.count(arr[i])
#     list.append(b)
# a=list.index(max(list))
# print(a)
maxx=[]
maxx.append(arr.count(1))
maxx.append(arr.count(2))
maxx.append(arr.count(3))
maxx.append(arr.count(4))
maxx.append(arr.count(5))
print(1+maxx.index(max(maxx)))