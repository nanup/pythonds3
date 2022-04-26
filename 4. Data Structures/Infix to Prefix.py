from pythonds3 import Stack

def infix_to_prefix(infix_string):
    
    token_list = infix_string.split()

    prefix_list = []
    op_stack = Stack()

    prec = {}
    prec["/"] = 3
    prec["*"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    for token in token_list:

        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefix_list.append(token)
        
        elif token == "(":
            while (not op_stack.is_empty()) and (prec[token] <= prec[op_stack.peek()]):
                prefix_list.append(op_stack.pop())
            op_stack.push(token)

        elif token == ")":
            while not op_stack.peek() == "(":
                prefix_list.insert(0, op_stack.pop())
            op_stack.pop()

        else:
            while (not op_stack.is_empty()) and (prec[token] <= prec[op_stack.peek()]):
                prefix_list.insert(0, op_stack.pop())
            op_stack.push(token)


    while not op_stack.is_empty():
        prefix_list.insert(0, op_stack.pop())

    return " ".join(prefix_list)

print(infix_to_prefix("( A + B ) * E + ( C + D )"))