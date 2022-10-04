class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        node = self.root

        if node == None:
            node = new_node
            self.root = node
        else:
            while True:
                if new_node.value < node.value:
                    if node.left is None:
                        node.left = new_node
                        break
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = new_node
                        break
                    else:
                        node = node.right


bi_tree = BinaryTree()
bi_tree.insert(9)
bi_tree.insert(4)
bi_tree.insert(6)
bi_tree.insert(20)
bi_tree.insert(170)
bi_tree.insert(15)
bi_tree.insert(1)
print(bi_tree)