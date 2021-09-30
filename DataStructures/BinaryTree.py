class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.value=val
class Tree:
    def __init__(self):
        self.root = None

    def add(self, val, r = None):
        if self.root == None:
            self.root = Node(val)
            return

        if r == None:
            r = self.root

        if val > r.value:
            if r.right == None:
                r.right = Node(val)
            else:
                self.add(val, r.right)

        else:
            if r.left == None:
                r.left = Node(val)
            else:
                self.add(val, r.left)
        return r
    def leftmost(self,r=None):
        if self.root==None:
            return
        elif r==None:
            return self.leftmost(self.root)
        else:
            if r.left!=None:
                return self.leftmost(r.left)
            else:
                return r
    def rightmost(self,r=None):
        if self.root==None:
            return
        elif r==None:
            return self.rightmost(self.root)
        else:
            if r.right!=None:
                return self.rightmost(r.right)
            else:
                return r
    def inorder(self, r=None):
        if r == None:
            r = self.root

        print(r.value)

        if r.left != None:
            self.inorder(r.left)

        if r.right != None:
            self.inorder(r.right)




    def delete(self,val,root=None):
        if self.root==None and root==None:
            return
        elif self.root!=None and root==None:
            root=self.root
        if root.right != None and root.right.value == val:
            print("node deleted is {0}".format(root.right.value))
            r=self.leftmost(root.right.right)
            r.right=root.right.right
            r.left=root.right.left
            root.right=r

        elif root.left != None and root.left.value == val:
            print("node deleted is {0}".format(root.left.value))
            r=self.rightmost(root.left.left)
            r.right=root.left.right
            r.left=root.left.left
            root.left=r
            
        elif val>root.value:
            return self.delete(val, root.right)
    
        else:
            return self.delete(val, root.left)

    
tree=Tree()
tree.add(10)
tree.add(4)
tree.add(28)
tree.add(0)
tree.add(8)
tree.add(24)
tree.add(32)
tree.add(16)
tree.add(12)
tree.add(20)
print(tree.root.left.left.value)
print(tree.root.right.left.value)

tree.delete(24)
print(tree.root.right.left.value)
print(tree.root.left.left.value)
print(tree.root.left.value)
