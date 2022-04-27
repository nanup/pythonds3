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

class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def add(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        
        while current is not None and item > current.data:
            previous = current
            current = current.next

        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return count

my_list = OrderedList()
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print(my_list.size())
print(my_list.search(93))
print(my_list.search(100))