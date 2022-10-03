class Node:

    def __init__(self, value):
        self.data = value
        self.next = None
        self.previous = None

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
        node.previous = self.tail
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head.previous = node
        self.head = node
        self.length += 1

    def pop_left(self):
        self.head = self.head.next
        self.length -= 1
        
    def insert(self, index, value):
        new_node = Node(value)
        node = self.head
        i = 0

        while i < index :
            previous = node
            node = node.next
            i += 1

        previous.next = new_node
        new_node.next = node
        self.length += 1

    def remove(self, index):
        if index > 0 and index < self.length:
            node = self.head
            i = 0

            while i < index :
                previous = node
                node = node.next
                i += 1

            previous.next = node.next
            self.length -= 1
        else:
            raise Exception('Index out of range.')

                

my_linked_list = LinkedList(10)
my_linked_list.append(30)
# my_linked_list.append(56)
# my_linked_list.append(564)
# my_linked_list.append(64)
my_linked_list.prepend(1)
print(my_linked_list)
# my_linked_list.pop_left()
# my_linked_list.insert(2,403)
# my_linked_list.insert(4, 5000)
# my_linked_list.remove(4)
# print(my_linked_list)
# print(my_linked_list.length)