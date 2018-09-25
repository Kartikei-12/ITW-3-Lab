#Author: Kartikei Mittal
#ID: 2017KUCP1032
#Date: 25-09-2018
#In order traversal in Binary Serch Tree

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
    
    def showNode(self):
        print("Value:", self.val)


class BST:
    def __init__(self):
        self.root=Node()

    def inOrderTraversal(self, node=None):
        if node is not None:
            node.showNode()
            self.inOrderTraversal(node.left)
            self.inOrderTraversal(node.right)

    def newNode(self, root, val=0):
        if root is None:
            root = Node(val)
        else:
            if root.val < val:
                if root.right is None:
                    root.right = Node(val)
                else:
                    self.newNode(root.right, val)
            else:
                if root.left is None:
                    root.left = Node(val)
                else:
                    self.newNode(root.left, val)
        


Tree = BST()
for i in range(1, 10):
    Tree.newNode(root=Tree.root, val=i)

Tree.inOrderTraversal()
