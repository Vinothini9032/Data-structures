'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Binarytree:
    def __init__(self):
        self.root=None
    def add(self,data):
        if self.root is None:
            self.root=Node(data)
            return
        self.recursiveadd(data,self.root)
    def recursiveadd(self,data,node):
        if node.left is None:
            node.left=Node(data)
        elif node.right is None:
            node.right=Node(data)
        else:
            self.recursiveadd(data,node.left)
    def remove(self,data):
        if self.root==None:
            print("Tree is Empty")
        if self.root==data:
            self.root=None
        self.recursive(data,self.root)
    def recursive(self,data,node):
        if node.left is not None and node.left.data==data:
            node.left=None
        if node.right is not None and node.right.data==data:
            node.right=None
        if node.left:
            self.recursive(data,node.left)
        if node.right:
            self.recursive(data,node.right)
    def search(self,data):
        nodefound=self.recursivesearch(data,self.root)
        if nodefound:
            print(True)
        else:
            print(False)
    def recursivesearch(self,data,node):
        if node is not None or node.data==data:
            return node
        return self.recursivesearch(data,node.left) or self.recursivesearch(data,node.right)
    def display(self,depth=0,node=None):
        if node is None:
            node=self.root
        print(" "*depth,node.data)
        if node.left is not None:
            self.display(depth+1,node.left)
        if node.right is not None:
            self.display(depth+1,node.right)
binarytree=Binarytree()
binarytree.add(5)
binarytree.add(4)
binarytree.add(3)
binarytree.add(2)
binarytree.add(1)
binarytree.add(0)
binarytree.display()
binarytree.remove(2)
binarytree.display()
binarytree.search(1)


            

