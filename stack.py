class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

    def __repr__(self):
        return self.data


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __repr__(self):
        nodes = []
        current_node = self.top
        while current_node is not None:
            nodes.append(current_node.data)
            current_node = current_node.next

        nodes = [str(x) for x in nodes]
        nodes.append('None')

        return ' -> '.join(nodes)

    def push(self, value):
        if self.length == 0:
            self.bottom = Node(value)
            self.top = self.bottom
            self.length += 1
        else:
            node = Node(value)
            node.next = self.top
            self.top = node
            self.length += 1

    def peek(self):
        if self.length > 0:
            return self.top.data
        else:
            raise Exception('Stack is empty')

    def pop(self):
        self.top = self.top.next
        self.length -= 1


    

        
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.pop()
my_stack.pop()
print(my_stack)
print(my_stack.peek())
print(my_stack.length)