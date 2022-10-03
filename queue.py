class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

    def __repr__(self):
        return self.data


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __repr__(self):
        nodes = []
        current_node = self.first
        while current_node is not None:
            nodes.append(current_node.data)
            current_node = current_node.next

        nodes = [str(x) for x in nodes]
        nodes.append('None')

        return ' -> '.join(nodes)

    def enqueue(self, value):
        if self.length == 0:
            self.first = Node(value)
            self.last = self.first
            self.length += 1
        else:
            node = Node(value)
            self.last.next = node
            self.last = node
            self.length += 1

    def peek(self):
        if self.length > 0:
            return self.first.data
        else:
            raise Exception('Stack is empty')

    def dequeue(self):
        self.first = self.first.next
        self.length -= 1


    

        
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.dequeue()
print(my_queue)
print(my_queue.peek())
print(my_queue.length)