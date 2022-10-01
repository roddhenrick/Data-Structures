from dataclasses import dataclass


class LinkedList:
    def __init__(self, data):
        self.head = {
            'data': data,
            'next_node': None
        }
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        return f"head = {{data: {self.head['data']}, next: {self.head['next_node']}}}"

    def append(self, value):
        node = {
            'data': value,
            'next_node': None
        }
        self.tail['next_node'] = node
        self.tail = node

        

my_linked_list = LinkedList(10)
my_linked_list.append(30)
my_linked_list.append(56)
print(my_linked_list)