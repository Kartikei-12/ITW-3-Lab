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

    @staticmethod
    def iOT(node=None):
        if node:
            BST.iOT(node.left)
            node.showNode()
            BST.iOT(node.right)

    def inOrderTraversal(self):
        BST.iOT(self.root)

    @staticmethod
    def nN(root, val=0):
        if root is None:
            root = Node(val)
        else:
            if root.val < val:
                if root.right is None:
                    root.right = Node(val)
                else:
                    BST.nN(root.right, val)
            else:
                if root.left is None:
                    root.left = Node(val)
                else:
                    BST.nN(root.left, val)
    
    def newNode(self, val):
        BST.nN(self.root, val)


Tree = BST()
for i in range(1, 10):
    Tree.newNode(val=i)

Tree.inOrderTraversal()
