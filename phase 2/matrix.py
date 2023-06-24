#using functions:
def mat(matrix,m,n):
    print("Enter the entries rowwise:")
    for i in range(m):
        a =[]
        for j in range(n):
            a.append(int(input()))
        matrix.append(a)
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end = " ")
        print(" ")
def dia(matrix,m,n):
    for i in range(m):
        for j in range(n):
            if(i==j):
                print(matrix[i][j],end=" ")
            else:
                print(" ",end=" ")
        print(" ")
def ndia(matrix,m,n):
    for i in range(m):
        for j in range(n):
            if(i!=j):
                print(matrix[i][j],end=" ")
            else:
                print(" ",end=" ")
        print(" ")
def upper(matrix, m, n):
    for i in range(m):
      for j in range(n):
          if (i < j):
                print(matrix[i][j], 
                       end = " " )
          else:
              print(" ",end=" ")
      print(" ")
def lower(matrix, m, n):
  for i in range(m):
      for j in range(n):
          if (i > j):
                print(matrix[i][j],end = " " )
          else:
              print("",end=" ")
      print("")
matrix=[]
m= int(input("Enter the number of rows:"))
n= int(input("Enter the number of columns:"))
print("the matrix:")
mat(matrix,m,n)
print("diagonal")
dia(matrix,m,n)
print("non diagonal")
ndia(matrix,m,n)
print("Lower triangular matrix: ")
lower(matrix, m, n)
print("Upper triangular matrix: ")
upper(matrix, m, n)
'''r=int(input("Enter no of the rows:"))
c=int(input("Enter no of the columns:"))
matrix=[]
for i in range(r):
    a=[]
    for i in range(c):
        x=int(input("Enter the item:"))
        a.append(x)
    matrix.append(a)
print("The Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
print("The diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i==j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Non diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i!=j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Upper diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i<j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Lower diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i>j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Transpose Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[j][i],end=" ")
    print()
# print("The Addition ")
'''
