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
        branch_root  = self.root

        while True:
            if node is None:
                break

            if value == node.value:
                if branch_root.left and branch_root.left.value == value:
                    branch = branch_root.left

                if branch_root.right and branch_root.right.value == value:
                    branch = branch_root.right

                subtree = branch.left
                rightmost_subtree = subtree.right
                previous = rightmost_subtree

                while rightmost_subtree is not None:
                    previous = rightmost_subtree
                    rightmost_subtree = rightmost_subtree.right

                rightmost_subtree = previous
                
                while True:
                    
                    if subtree is not None:
                        rightmost_subtree.right = branch.right
                        if branch == branch_root.right:
                            branch_root.right = subtree
                        else:
                            branch_root.left = subtree
                        break
                    else:
                        if branch == branch_root.right:
                            branch_root.right = None
                        else:
                            branch_root.left = None
                        break
                break

            elif value < node.value:
                branch_root = node
                node = node.left
            elif value > node.value:
                branch_root = node
                node = node.right



bi_tree = BinaryTree()
bi_tree.insert(60)
bi_tree.insert(30)
bi_tree.insert(51)
bi_tree.insert(38)
bi_tree.insert(55)
bi_tree.insert(44)
bi_tree.insert(54)
bi_tree.insert(72)
bi_tree.insert(73)
bi_tree.insert(78)
bi_tree.insert(85)
bi_tree.insert(86)
bi_tree.insert(90)
bi_tree.insert(99)
bi_tree.remove(51)
print(bi_tree)
