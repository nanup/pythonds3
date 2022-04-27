class Node:
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node

    next = property(get_next, set_next)

    def set_data(self, node_data):
        self._data = node_data

    def get_data(self):
        return self._data

    data = property(get_data, set_data)

    def __str__(self):
        return str(self._data)

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                previous.next = current.next
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
                
my_list = UnorderedList()

my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print(my_list.size())
print(my_list.search(93))
print(my_list.search(100))

my_list.add(100)
print(my_list.search(100))
print(my_list.size())

my_list.remove(54)
print(my_list.size())
my_list.remove(93)
print(my_list.size())
my_list.remove(31)
print(my_list.size())
print(my_list.search(93))

try:
    my_list.remove(27)
except ValueError as ve:
    print(ve)