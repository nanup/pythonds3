import operator
from pythonds3 import Stack
from pythonds3 import BinaryTree

def build_parse_tree(expr):
    token_list = expr.split()
    stk = Stack()
    bt = BinaryTree("")
    stk.push(bt)
    current_tree = bt

    for i in token_list:
        if i  == "(":
            current_tree.insert_left("")
            stk.push(current_tree)
            current_tree = current_tree.left_child

        elif i in ["+", "-", "*", "/"]:
            current_tree.set_root_val(i)
            current_tree.insert_right("")
            stk.push(current_tree)
            current_tree = current_tree.right_child

        elif i == ")":
            current_tree = stk.pop()

        elif i not in ["+", "-", "*", "/", ")"]:
            try:
                current_tree.root = int(i)
                parent = stk.pop()
                current_tree = parent
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return bt

def evaluate(parse_tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv 
    }

    left_child = parse_tree.left_child
    right_child = parse_tree.right_child

    if left_child and right_child:
        fn = operators[parse_tree.root]
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.root

pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(evaluate(pt))