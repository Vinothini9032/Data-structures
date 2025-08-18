class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Binarysearch:
    def __init__(self):
        self.root=None
    def add(self,data):
        if self.root is None:
            self.root=Node(data)
            return
        self.readd(data,self.root)
    def readd(self,data,node):
        if data<node.data:
            if node.left is None:
                node.left=Node(data)
            else:
                self.readd(data,node.left)
        elif data>node.data:
            if node.right is None:
                node.right=Node(data)
            else:
                self.readd(data,node.right)
    def display(self):
        result=[]
        self.inorderTraversal(self.root,result)
        print(result)
    def inorderTraversal(self,node,result):
        if not node:
            return None
        else:
            self.inorderTraversal(node.left,result)
            result.append(node.data)
            self.inorderTraversal(node.right,result)
    def preorderTraversal(self,node,result):
        if not node:
            return None
        else:
            result.append(node.data)
            self.preorderTraversal(node.left,result)
            self.preorderTraversal(node.right,result)
    def postorderTraversal(self,node,result):
        if not node:
            return None
        else:
            self.postorderTraversal(node.left,result)
            self.postorderTraversal(node.right,result)
            result.append(node.data)
    def remove(self,data):
        if not self.root:
            print("Tree is empty")
            return 
        if self.root==data:
            self.root=None
        self.reremove(data,self.root)
    def reremove(self,data,node):
        if node.left and node.left.data==data:
            node.left=None
        if node.right and node.right.data==data:
            node.right=None
        elif data<node.data:
            self.reremove(data,node.left)
        elif data>node.data:
            self.reremove(data,node.right)
    def search(self,data):
        s=self.research(data,self.root)
        if s:
            print(True)
        else:
            print(False)
    def research(self,data,node):
        if node is None:
            return
        if node and node.data==data:
            return node
        elif data<node.data:
            return self.research(data,node.left)
        elif data>node.data:
             return self.research(data,node.right)
            
    
binary=Binarysearch()
binary.add(45)
binary.add(5)
binary.add(50)
binary.add(35)
binary.add(47)
binary.add(49)
binary.display()
binary.remove(35)
binary.display()
binary.search(5)