#Author: Kartikei Mittal
#ID: 2017KUCP1032
#Date: 25-09-2018
#In order traversal in Binary Serch Tree

class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
 
def inorderTraversal(tree, node):
    if tree is None:
        tree = node
    else:
        if tree.value < node.value:
            if tree.right is None:
                tree.right = node
            else:
                inOrderTraversal(tree.right, node)
        else:
            if tree.left is None:
                tree.left = node
            else:
                inOrderTraversal(tree.left, node)
 
def show(tree):
    if tree:
        show(tree.left)
        print(tree.value)
        show(tree.right)
 
root = Node(0)
for i in range(1, 10):
    inOrderTraversal(root,Node(i))
 
show(root)
