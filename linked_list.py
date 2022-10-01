from dataclasses import dataclass


class LinkedList:
    def _node(self, data):
        node = {
            'data': data,
            'next_node': None
        }
        return node

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
        node = self._node(value)
        self.tail['next_node'] = node
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = self._node(value)
        node['next_node'] = self.head
        self.head = node
        self.length += 1

        

my_linked_list = LinkedList(10)
my_linked_list.append(30)
my_linked_list.append(56)
my_linked_list.prepend(1)
print(my_linked_list)