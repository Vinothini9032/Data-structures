class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinarySearch:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
            return
        cur=self.root
        while True:
            if data<cur.data:
                if cur.left is not None:
                    cur=cur.left
                else:
                    cur.left=Node(data)
                    break
            elif data>cur.data:
                if cur.right is not None:
                    cur=cur.right
                else:
                    cur.right=Node(data) 
                    break
    def delete(self,root,key):
        parent=None
        cur=root
        while cur and cur.data != key:
            parent=cur
            if key<cur.data:
                cur=cur.left
            else:
                cur=cur.right
        if not cur:
            return root
        if cur.left and cur.right:
            successor=cur
            succ=cur.right
            while succ.left:
                successor=succ
                succ=succ.left
            cur.data=succ.data
            cur,parent=succ,successor
        child=cur.left if cur.left else cur.right
        if not parent:
            return child
        if parent.left==cur:
            parent.left=child
        else:
            parent.right=child
        return root
    def deletenode(self,key):
        self.root=self.delete(self.root,key)
    
        


    def display(self):
        result=[]
        self.inorder(self.root,result)
        print(result)
    def inorder(self,node,result):
        if not node:
            return 
        
        self.inorder(node.left,result)
        result.append(node.data)
        self.inorder(node.right,result)
binary=BinarySearch()
binary.insert(3)
binary.insert(9)
binary.insert(6)
binary.insert(7)
binary.display()
binary.deletenode(6)


