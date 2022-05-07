from pythonds3 import BinarySearchTree

class AVLTreeNode(BinarySearchTree):
    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.left_child)
        else:
            if current_node.right_child:
                    self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        if node.balance_factor > +1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        else:
            if node.parent:
                if node.is_left_child():
                    node.parent.balance_factor += 1
                elif node.is_right_child():
                    node.parent.balance_factor -= 1
                if node.parent.balance_factor != 0:
                    self.update_balance(node.parent)
    
    def rotate_right(self, rotation_root):
        new_root = rotation_root.left_child
        rotation_root.left_child = new_root.right_child
        if new_root.right_child:
            new_root.right_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root
        new_root.right_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = rotation_root.balance_factor - 1 + max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 - min(rotation_root.balance_factor, 0)

    def rotate_left(self, rotation_root):
        new_root = rotation_root.right_child
        rotation_root.right_child = new_root.left_child
        if new_root.left_child:
            new_root.left_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root
        new_root.left_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rotation_root.balance_factor, 0)

    def rebalance(self, node):
        if node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
            self.rotate_right(node)
        elif node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
            self.rotate_left(node)