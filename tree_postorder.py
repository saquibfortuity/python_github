class node:
    def __init__(self,val):
        self.leftchild = None
        self.rightchild = None
        self.nodedata = val


root = node(1)
root.leftchild = node(2)
root.rightchild = node(3)
root.leftchild.leftchild = node(4)
root.leftchild.rightchild = node(5)

def preorder(root):
    if root:
        preorder(root.leftchild)
        preorder(root.rightchild)
        print(root.nodedata)


preorder(root)


