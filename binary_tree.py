import json

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def __repr__(self) -> str:
        return json.dumps(self.traverse(self.root), indent= 3)

    def traverse(self, node):
        if not node == None:
            tree = {'value': node.value}
            tree["left"] = node.left is None if None else self.traverse(node.left)
            tree["right"] = node.right is None if None else self.traverse(node.right)
            return tree

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

    def lookup(self, value):
        node = self.root

        while True:
            if node is None:
                break

            if value == node.value:
                return node
            elif value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right

        return 'Node not found.'

    def remove(self, value):
        node = self.root
        parent  = None

        if node is None:
            return "Empty Tree"

        while True:

            if value < node.value:
                parent = node
                node = node.left
            elif value > node.value:
                parent = node
                node = node.right
            elif node.value == value:
                if not (node.left or  node.right):
                    if parent.left and parent.left.value == value:
                        parent.left = None
                    else:
                        parent.right = None
                    return
                elif node.left and node.right:
                    leftmost = self._find_min(node.right)

                elif node.left or node.right:
                    if node.left:
                        node = node.left
                    else:
                        node = node.right

                    if parent.left.value == value:
                        parent.left = node
                    else:
                        parent.right = node
                    return
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node.value

                        



bi_tree = BinaryTree()
bi_tree.insert(15)
bi_tree.insert(10)
bi_tree.insert(8)
bi_tree.insert(12)
bi_tree.insert(6)
bi_tree.insert(11)
bi_tree.insert(20)
bi_tree.insert(17)
bi_tree.insert(25)
bi_tree.insert(16)
bi_tree.insert(27)
print(bi_tree.remove(15))

print(bi_tree)
