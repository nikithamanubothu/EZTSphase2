def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a
b=[2,3,1,4]
s=bubble(b)
print(s)