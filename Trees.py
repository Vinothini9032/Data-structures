'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[] #no of nodes..one to multiple
class Tree:
    def __init__(self):
        self.root=None
    def add(self,data,parentdata=None):
        node=TreeNode(data)
        if self.root is None:
            self.root=node
            return
        parentnode=self.findNode(parentdata,self.root)
        if parentnode is None:
            print("Parentnode is notfound")
        parentnode.children.append(node)
    def findNode(self,data,node):
        if node.data==data:
            return node
        for child in node.children:
            nodeFound=self.findNode(data,child)
            if nodeFound is not None:
                return nodeFound
        return None
    def display(self,depth=0,node=None):
        if not node:#root node ku
            node=self.root
        print(" "*depth,node.data)# node place la entha value oh athu pass aagum for example first node =root node
        for child in node.children:
            self.display(depth+1,child)
    def remove(self,data):
        if not self.root:#root empty ah iruntha tree empty
            print("Tree if empty")
            return 
        if self.root.data==data:#root empty panitalu antha tree full ah delete ayuru
            self.root=None
            return 
        parentnode=self.findparentnode(data,self.root)
        if parentnode is not None:
            for child in parentnode.children:
                if child.data==data:
                    parentnode.children.remove(child)
        print("node is not found")
    def findparentnode(self,data,node):
        for child in node.children:
            if child.data==data:
                return node
            nodefound=self.findparentnode(data,child)
            if notfound:
                return nodefound
        return None
tree=Tree()
tree.add(5)
tree.add(7,5)
tree.add(6,7)
tree.display()
tree.remove(7)
tree.display()
    