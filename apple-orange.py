x=list()
y=list()
co=0
c=0

s = int(input())

t = int(input())

a = int(input())

b = int(input())

m = int(input())

n = int(input())

apples = [-2,2,1]

oranges = [5,-6]
for i in apples:
    w=a-i
    x.append(w)
print(x)
for j in oranges:
    e=b-j
    y.append(e)
print(y)
for f in x:
    if (f>=a and f<=b):
        co+=1
        print(co)
    else:
        print(co)
for h in y:
    if (h>=a and h<=b):
        c+=1
        print(c)
    else:
        pass
