class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Cll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_start(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            new.next=self.head
            self.head=new
            self.tail.next=self.head
    def insert_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head
    def insert_pos(self,pos,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            if pos==1:
                insert_start()
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                new.next=temp.next
                temp.next=new
    def delete_beginning(self):
        if self.head is None:
            print("circular list is empty")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.tail.next=self.head
    def delete_end(self):
        '''temp=self.head.next
        prev=self.head'''
        if self.head is None:
            print("circular list is empty")
        else:
            if(self.head != self.tail ):    
                temp = self.head
                while(temp.next != self.tail):    
                    temp = temp.next  
                self.tail = temp   
                self.tail.next = self.head  
            else:    
                self.head = self.tail = None
        '''else:
            while temp.next!=self.head:
                temp=self.head.next
                prev=self.head
            temp.next=None
            self.tail=prev
            self.tail.next=self.head'''
    def delete_pos(self,pos):
        if self.head is None:
            print("circular list is empty")
        elif pos==1:
            delete_end()
        else:
            temp=self.head.next
            prev=self.head
            for i in range(1,pos-1):
                temp=temp.next
                prev=prev.next
            prev.next=temp.next
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
cl=Cll()
n=Node(10)
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
cl.head=n
cl.tail=n5
cl.tail.next=cl.head
'''print(n5.next)
print(cl.tail.next)
print(n)
print(n.data,n1.data,n2.data,n3.data,n4.data,n5.data,end=" ")'''
print("The Circular Linked List before insertion:")
cl.display()
print("The Circular Linked List After Inserting at the starting:")
cl.insert_start(5)
cl.display()
print("The Circular Linked List After Inserting at the ending:")
cl.insert_end(70)
cl.display()
print("The Circular Linked List After Inserting at the specific position:")
cl.insert_pos(3,25)
cl.display()
print("The Circular Linked List After deleting at the beginning:")
cl.delete_beginning()
cl.display()
print("The Circular Linked List After deleting at the ending:")
cl.delete_end()
cl.display()
print("The Circular Linked List After deleting at the specific position:")
cl.delete_pos(2)
cl.display()


        
