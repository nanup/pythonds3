from pythonds3 import BinaryTree

def preorder(bt):
    if bt:
        print(bt.root)
        preorder(bt.left_child)
        preorder(bt.right_child)

def postorder(bt):
    if bt:
        preorder(bt.left_child)
        preorder(bt.right_child) 
        print(bt.root)

def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())

bt = BinaryTree(20)
bt.insert_left(5)
bt.insert_right(10)
bt.insert_right(-9)
inorder(bt)