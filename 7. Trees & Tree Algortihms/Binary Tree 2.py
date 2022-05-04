class BinaryTree:

    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child
    
    def get_root_val(self):
        return self.root

    def set_root_val(self, root):
        self.root = root

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

a_tree = BinaryTree("a")
print(a_tree.get_root_val())
print(a_tree.get_left_child())
a_tree.insert_left("b")
print(a_tree.get_left_child())
print(a_tree.get_left_child().get_root_val())
a_tree.insert_right("c")
print(a_tree.get_right_child())
print(a_tree.get_right_child().get_root_val())
a_tree.get_right_child().set_root_val("hello")
print(a_tree.get_right_child().get_root_val())