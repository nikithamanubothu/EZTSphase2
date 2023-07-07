'''
def search(root,key):
    if root is None or root.val==key:
        return root
    if root.val<key:
        return search(root.right,key)
    return search(root.left,key)'''

class Node:
    def _init_(self,key):
        self.key=key
        self.left=None
        self.right=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            print("empty")
            return 
        if self.key==data:
            print("skip")
            return 
        if self.key>data:
            if self.left:
                self.left.insert(data)
            else:
                self.left=Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right=Node(data)
    def pre_order(self):
        print(self.key,end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
    def post_order(self):
        print(self.key,end=" ")
        if self.right:
            self.right.post_order()
        if self.left:
            self.left.post_order()
    def in_order(self):
        if self.left:
            self.left.pre_order()
        if self.key:
            print(self.key,end=" ")
        if self.right:
            self.right.pre_order()
    def delete(self,key):
        if self.key is None:
            print("can not delete")
        else:
            if key <self.key:
                if self.left:
                    self.left=self.left.delete(key)
                else:
                    print("\ngiven node {key} is not there")
            elif key > self.key:
                if self.right:
                    self.right=self.right.delete(key)
                else:
                    print("\ngiven node {key} is not there")
            else:
                if self.left is None:
                    temp=self.right
                    self=None
                    return temp
                elif self.right is None:
                    temp=self.left
                    self=None
                    return temp
                n=self.right
                while n.left:
                    n=n.left
                self.key=n.key
                self.right=self.right.delete(key)
            return self              
root=Node(45)
root.insert(30)
root.insert(50)
root.insert(10)
root.insert(60)
root.insert(20)
root.insert(70)
root.pre_order()
print("\n")
root.post_order()
print("\n")
root.in_order()
root.delete(50)
print("\n")
root.pre_order()
#print(root)