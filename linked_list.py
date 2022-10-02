class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        nodes = []
        current_node = self.head
        while current_node is not None:
            nodes.append(current_node.data)
            current_node = current_node.next

        nodes = [str(x) for x in nodes]
        nodes.append('None')

        return ' -> '.join(nodes)

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