'''#Gomathi mam's code:
class node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class sll:
    def __init__ (self):
        self.head=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            #while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
            #This code helps to avoid arrow at the end
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" -> ")
                else:
                    print(temp.data,end=" ")
            #temp.data means first node's data
                temp=temp.next
obj=sll()
n=node(10)
obj.head=n
n1=node(20)
n.next=n1
obj.display()'''

#sahil sangole sir's codee
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
n=Node(10)
sl=SLL()
sl.head=n
n1=Node(20)
n.next=n1
print(n.next)
sl.display()

