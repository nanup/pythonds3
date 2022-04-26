from pythonds3 import Deque

def is_palindrome(a_string):
    a_deque = Deque()
    for ch in a_string:
        a_deque.add_rear(ch)
    while a_deque.size() > 1:
        if a_deque.remove_front() != a_deque.remove_rear():
            return False
    return True
        
print(is_palindrome("naan"))