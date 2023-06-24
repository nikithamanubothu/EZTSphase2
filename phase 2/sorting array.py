#given an array of size n which contains elements as 0&1 sort the array:
n=int(input())
l=[]
nm=[]
for i in range(n):
    e=int(input("enter element"))
    l.append(e)
while l:
    m=l[0]
    for j in l:
        if j<m:
            m=j
    nm.append(m)
    l.remove(m)
print(nm)
