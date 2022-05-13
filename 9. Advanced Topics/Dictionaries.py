from random import randrange
from pythonds3 import Stack

def flip():
    return randrange(2)

class HeaderNode:
    def __init__(self):
        self._next = None
        self._down = None

    @property
    def next(self):
        return self._next

    @property
    def down(self):
        return self._down

    @next.setter
    def next(self, value):
        self._next = value

    @down.setter
    def down(self, value):
        self._down = value

class DataNode:
    def __init__(self, key, value):
        self._key = key
        self._data = value
        self._next = None
        self._down = None

    @property
    def next(self):
        return self._next

    @property
    def down(self):
        return self._down

    @property
    def key(self):
        return self._key

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @next.setter
    def next(self, value):
        self._next = value

    @down.setter
    def down(self, value):
        self._down = value

class SkipList:
    def __init__(self):
        self._head = None

    def search(self, key):
        current = self._head

        while current:
            if current.next is None:
                current = current.down
            else:
                if current.next.key == key:
                    return current.next.data
                else:
                    if key < current.next.key:
                        current = current.down
                    else:
                        current = current.next

        return None

    

    def insert(self, key, value):
        if self.head is None:
            self.head = HeaderNode()
            temp = DataNode(key, value)
            self.head.next = temp
            top = temp
            while flip() == 1:
                newhead = HeaderNode()
                temp = DataNode(key, value)
                temp.down = top
                newhead.next = temp
                newhead.down = self.head
                self.head = newhead
                top = temp
        else:
            tower = Stack()
            current = self.head
            while current:
                if current.next is None:
                    tower.push(current)
                    current = current.down
                else:
                    if current.next.key > key:
                        tower.push(current)
                        current = current.down
                    else:
                        current = current.next

            lowest_level = tower.pop()
            temp = DataNode(key, value)
            temp.next = lowest_level.next
            lowest_level.next = temp
            top = temp

        while flip() == 1:
            if tower.is_empty():
                newhead = HeaderNode()
                temp = DataNode(key, value)
                temp.down = top
                newhead.next = temp
                newhead.down = self.head
                self.head = newhead
                top = temp
            else:
                next_level = tower.pop()
                temp = DataNode(key, value)
                temp.down = top
                temp.next = next_level.next
                next_level.next = temp
                top = temp

class Map:
    def __init__(self):
        self.collection = SkipList()

    def put(self, key, value):
        self.collection.insert(key, value)

    def get(self, key):
        return self.collection.search(key)