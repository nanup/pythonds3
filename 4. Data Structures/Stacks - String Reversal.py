import pythonds3

def rev_string(mystr):
    mystack = pythonds3.Stack()
    for ch in mystr:
        mystack.push(ch)
    
    revstr = ""

    while not mystack.is_empty():
        revstr += mystack.pop()
    
    return revstr

astr = "my name is nanu"
print(rev_string(astr))
