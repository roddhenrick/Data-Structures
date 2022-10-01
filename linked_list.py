class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        return f"head = {{data: {self.head.data}, next: {self.head.next}}}"

    def append(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def pop_left(self):
        self.head = self.head.next
        

my_linked_list = LinkedList(10)
my_linked_list.append(30)
my_linked_list.append(56)
my_linked_list.prepend(1)
my_linked_list.pop_left()
print(my_linked_list)