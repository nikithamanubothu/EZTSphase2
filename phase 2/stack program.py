n=int(input("enter the size of the stack"))
s=[]
def push_element():
    if len(s)==n:
        print("stack is full")
    else:
        print("enter the elements into the stack")
        element=int(input())
        s.append(element)
        print(s)
def pop_element():
    if not s:
        print("the stack is empty")
    else:
        e=s.pop()
        print(e,"removed")
        print(s)
while True:
    print("enter your choice \n1.push\n2.pop\n3quit")
    ch=int(input())
    if ch==1:
        push_element()
    elif ch==2:
        pop_element()
    elif ch==3:
        break
    else:
        print("enter correct choice")

        
