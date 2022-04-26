from pythonds3 import Stack

def infix_to_postfix(infix_string):
    
    token_list = infix_string.split()

    postfix_list = []
    op_stack = Stack()

    prec = {}
    prec["^"] = 4
    prec["/"] = 3
    prec["*"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    for token in token_list:

        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        
        elif token == "(":
            op_stack.push(token)

        elif token == ")":
            while not op_stack.peek() == "(":
                postfix_list.append(op_stack.pop())
            op_stack.pop()

        else:
            while (not op_stack.is_empty()) and (prec[token] <= prec[op_stack.peek()]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    while len(postfix_list) > 1:
        for ch in postfix_list:
            if ch in prec:
                print(postfix_list)
                pos = postfix_list.index(ch)

                op = postfix_list[pos]
                op1 = int(postfix_list[pos - 2])
                op2 = int(postfix_list[pos - 1])

                postfix_list.insert(pos, do_math(op, op1, op2))

                postfix_list.pop(pos + 1)
                postfix_list.pop(pos - 1)
                postfix_list.pop(pos - 2)
            
            continue

    return postfix_list[0]

def do_math(op, op1, op2):
    if op == "^":
        return op1 ** op2
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))