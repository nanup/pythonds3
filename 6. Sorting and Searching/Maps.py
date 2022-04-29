from random import randrange

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def put(self, key, data):
        slot = self.hash(key, len(self.slots))

        if self.slots[slot] is None:
            self.slots[slot] = key
            self.data[slot] = data
        else: 
            if self.slots[slot] == key:
                self.data[slot] = data #replace
            else:
                next_slot = self.rehash(slot, len(self.slots))
                while(
                    self.slots[next_slot] is not None and
                    self.slots[next_slot] != key
                ):
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        start_slot = self.hash(key, len(self.slots))
        position = start_slot

        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    return None

        return None

    def hash(self, key, size):
        return key % size

    def rehash(self,old_hash, size):
        return (old_hash + 1) % size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

def main():
    h = HashTable(11)
    h[54] = "cat"
    h[26] = "dog"
    h[93] = "lion"
    h[17] = "tiger"
    h[77] = "bird"
    h[31] = "cow"
    h[44] = "goat"
    h[55] = "pig"
    h[20] = "chicken"
    print(h[20])
    print(h[17])
    h[20] = "duck"
    print(h[20])
    print(h.data)
    print(h[99])
    
main()