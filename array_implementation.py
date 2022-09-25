class My_Array:
    def __init__(self, *args):
        self.length = 0
        self.data = {}

        if args:
            for arg in args:
                self.push(arg)

    def __str__(self):
        return f'{self.__class__}: {{ length: {self.length}, data: {self.data}}}'

    def __len__(self):
        return self.length

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index <= self.length -1:
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
    
    @property
    def list(self):
        return self.data

    def push(self, value):
        self.data[self.length] = value
        self.length += 1
        return self.length

    def pop(self):
        value = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return value

    def delete(self, index):
        item = self.data[index]
        self.shift_items(index)

    def shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1

arr = My_Array('a', 'b', 'c')
print(arr.list)

for i in arr:
    print(i)