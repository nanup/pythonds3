class ArrayList:
    def __init__(self):
        self.size_exponent = 0
        self.last_index = 0
        self.max_size = 0
        self.array_list = []

    def append(self, value):
        if self.last_index > self.max_size - 1:
            self.__resize()
        self.array_list[self.last_index] = value
        self.last_index += 1

    def __resize(self):
        new_size = 2 ** self.size_exponent
        print("new_size = " + new_size)
        new_array = [0] * new_size

        for i in range(self.max_size):
            new_array[i] = self.array_list[i]
        
        self.max_size = new_size
        self.array_list = new_array
        self.size_exponent += 1

    def __getitem__(self, idx):
        if self.last_index < self.max_size:
            return self.array_list[idx]
        raise LookupError("index out of bounds")

    def __setitem__(self, idx, value):
        if self.last_index < self.max_size:
            self.array_list[idx] = value
        raise LookupError("index out of bounds")

    def insert(self, idx, value):
        if self.last_index > self.max_size - 1:
            self.__resize()
        for i in range(self.last_index, idx - 1, -1):
            self.array_list[i + 1] = self.array_list[i]
        self.last_index += 1
        self.array_list[idx] = value
