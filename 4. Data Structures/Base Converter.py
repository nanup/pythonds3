from pythonds3.basic import Stack

def base_converter(num, base):
    digits = "0123456789ABCDEFGHIJKLMNOP"
    stk = Stack()
    while num > 0:
        rem = num % base
        stk.push(rem)
        num = num // base
    str = ""
    while not stk.is_empty():
        str += digits[stk.pop()]
    return str

print(base_converter(26, 26))