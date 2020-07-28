class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        output = []

        def walk(node):
            if not self:
                return
            output.append(node.value)
            walk(node.left)
            walk(node.right)
        walk(self.root)

        return output


    def max_value(self):
        if self.root:
            _max = self.root.value

            def traverse(node):
                nonlocal _max
                if node:
                    if node.value > _max:
                        _max = node.value
                    traverse(node.left)
                    traverse(node.right)
                    return _max

            traverse(self.root)
            return _max


class BST(BinaryTree):
    def add(self, value):

        def walk(node, node_to_add):
            if not node:
                return

            if node_to_add.value < node.value:
                #go left
                if not node.left:
                    node.left = node_to_add
            else:
                #go right
                if not node.right:
                    node.right = node_to_add
                else:
                    walk(node.right, node_to_add)

        n = Node(value)

        if not self.root:
            self.root = n
            return

        walk(self.root, n)



bst = BST()
bst.add(4)
bst.add(6)
bst.add(7)
bst.add(3)
bst.add(10)
bst.add(-1)
bst.add(50)
bst.add(34)
print(bst)
# print(bst.pre_order())
print(bst.max_value())
