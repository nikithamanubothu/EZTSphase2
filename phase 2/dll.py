class node:
    def __init__ (self,data):
        self.prev=None
        self.data=data
        self.next=None
class dll:
    def __init__ (self):
        self.head=None
    def insert_beginning(self,data):
        new=node(data)
        temp=self.head
        new.next=temp
        temp.prev=new
        self.head=new
    def insert_end(self,data):
        new=node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new
        new.prev=temp
        new.next=None
    def insert_pos(self,pos,data):
        new=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new.prev=temp
        new.next=temp.next
        temp.next.prev=new
        temp.next=new
    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next.prev=None
        temp.next=None
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None
    def delete_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        temp.prev=prev
        #prev.next=temp.next
        #temp.next=prev.next
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            '''while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next'''
            #This code helps to avoid arrow at the end
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" -><- ")
                else:
                    print(temp.data,end="")
            #temp.data means first node's data           
                temp=temp.next
o=dll()
n=node(10)
o.head=n
#print(n)
#print(n.data)
n1=node(20)
n.next=n1
n1.prev=n
#print(n1.prev)
#print(n1.data)
n2=node(30)
n1.next=n2
n2.prev=n1
#print(n2.data)
n3=node(40)
n2.next=n3
n3.prev=n2
#print(n3.data)
print("The Doubly Linked List Before Insertion:- ")
o.display()
print("\nThe Doubly linked List After Inserting at the beginning::-")
o.insert_beginning(5)
o.display()
print("\nThe Doubly linked List After Inserting at the ending::-")
o.insert_end(50)
o.display()
print("\nThe Doubly linked List After Inserting at the specific position::-")
o.insert_pos(2,15)
o.display()
print("\nThe Doubly linked List After Deleting at the beginning::-")
o.delete_beginning()
o.display()
print("\nThe Doubly linked List After Deleting at the ending::-")
o.delete_end()
o.display()
print("\nThe Doubly linked List After Deleting at the specific Position::-")
o.delete_pos(3)
o.display()
