k=1
b=0
c=7
bill=[3, 10, 2, 9]
z=bill[2]
print("this is z ",z)
a=bill[:k]+bill[k+1:]
for i in a:
    b+=i
print(b)
d=b//2
if d==c:
    print("Bon Apptid")
else:
    e=c-d
    print(e)
print(d)
print(a)