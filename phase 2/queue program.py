n=int(input("enter the size of the Queue"))
q=[]
def enqueue():
    if len(q)==n:
        print("Queue is full")
    else:
        print("enter the elements into the Queue")
        element=int(input())
        q.append(element)
        print(q)
def dequeue():
    if not q:
        print("the Queue is empty")
    else:
        e=q.pop(0)
        print(e,"removed")
        print(q)
while True:
    print("enter your choice \n1.Enqueue\n2.Dequeue\n3Quit")
    ch=int(input())
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        break
    else:
        print("enter correct choice")

        
