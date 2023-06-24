class node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class sll:
    def __init__ (self):
        self.head=None
    def insert_end(self,data):
        nb=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=nb
        nb.next=None
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
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
print("before insertion")
obj.display()
print("\nAfter insertion")
obj.insert_end(100)
obj.display()
