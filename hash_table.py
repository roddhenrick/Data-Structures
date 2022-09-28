class HashTable:
    def __init__(self, size):
        self.data = list((None for i in range(size)))
        self.length = 0
        self.keys = []

    def __len__(self):
        return self.length

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.length:
            item = self.keys[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)

        return hash

    def get(self, key):
        slot = self._hash(key)
        keys = len(self.data[slot])

        if keys == 1:
            return self.data[slot][0][1]
        else:
            for i in range(len(self.data[slot])):
                if self.data[slot][i][0] == key:
                    return self.data[slot][i][1]



    def set(self, key, value):
        if key == '':
            raise KeyError

        slot = self._hash(key)
        
        if not self.data[slot]:
            self.data[slot] = []

        self.data[slot].append([key, value])
        self.keys.append(key)
        self.length += 1
        return self.data

my_hash_table = HashTable(50)
table = my_hash_table.set('emerald', 'green')
table2 = my_hash_table.set('aquamarine', 'blue')
table3 = my_hash_table.set('amethyste', 'violet')
print(table)
print(my_hash_table.get('emerald'))
print(my_hash_table.get('aquamarine'))
print(my_hash_table._hash('amethyste'))

print(len(my_hash_table))

for key in my_hash_table:
    print(my_hash_table.get(key))