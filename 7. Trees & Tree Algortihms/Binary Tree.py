def make_binary_tree(root):
    return [root, [], []]

def insert_left(a_tree, new_child):
    old_child = a_tree.pop(1)
    if len(old_child) > 1:
        a_tree.insert(1, [new_child, old_child, []])
    else:
        a_tree.insert(1, [new_child, [], []])
    return a_tree

def insert_right(a_tree, new_child):
    old_child = a_tree.pop(2)
    if len(old_child) > 1:
        a_tree.insert(2, [new_child, old_child, []])
    else:
        a_tree.insert(2, [new_child, [], []])
    return a_tree

def get_root_val(a_tree):
    return a_tree[0]

def set_root_val(a_tree, new_value):
    a_tree[0] = new_value

def get_left_child(a_tree):
    return a_tree[1]

def get_right_child(a_tree):
    return a_tree[2]

a_tree = make_binary_tree(3)
insert_left(a_tree, 4)
insert_left(a_tree, 5)
insert_right(a_tree, 6)
insert_right(a_tree, 7)
left_child = get_left_child(a_tree)
print(left_child)

set_root_val(left_child, 9)
print(a_tree)
insert_left(left_child, 11)
print(a_tree)
print(get_right_child(get_right_child(a_tree)))