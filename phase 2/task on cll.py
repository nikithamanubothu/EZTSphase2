'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Cll:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        temp=self.head
        if self.head is None:
            print("Circular Linked List is Empty")
        else:
            print(temp.data,"->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"->",end=" ")
            print(temp.next.data)
    def detect_loop(self):
        if cl.tail.next==self.head:
            print("loop exists")
        else:
            print("their is no loop")
cl=Cll()
n=Node(1)
n1=Node(2)
n.next=n1
n2=Node(3)
n1.next=n2
n3=Node(4)
n2.next=n3
cl.head=n1
cl.tail=n3
cl.tail.next=cl.head
print("The Circular Linked List:")
cl.display()
cl.detect_loop()'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Cll:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        temp=self.head
        if self.head is None:
            print("Circular Linked List is Empty")
        else:
            print(temp.data,"->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"->",end=" ")
            print(temp.next.data)
    def detect_loop(self):
        if cl.head.next==self.tail:
            print("loop exists")
        else:
            print("their is no loop")
cl=Cll()
n=Node(4)
n1=Node(5)
n.next=n1
n2=Node(7)
n1.next=n2
n3=Node(8)
n2.next=n3
cl.head=n3
cl.tail=n1
cl.head.next=cl.tail
print("The Circular Linked List:")
cl.display()
cl.detect_loop()'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Cll:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        temp=self.head
        if self.head is None:
            print("Circular Linked List is Empty")
        else:
            print(temp.data,"->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"->",end=" ")
            print(temp.next.data)
    #def length_list(self):
        
cl=Cll()
n=Node(1)
n1=Node(2)
n.next=n1
n2=Node(3)
n1.next=n2
n3=Node(4)
n2.next=n3
cl.head=n1
cl.tail=n3
cl.tail.next=cl.head
print("The Circular Linked List:")
cl.display()
cl.length_list()
cl.display()



        

        
