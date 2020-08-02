  
class _Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self._root = None


def fizz_buzz(value):

    if value % 15 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    else:
        return str(value)

def fizz_buzz_tree(tree):

    new_tree = BinaryTree()

    if not tree._root:
        return new_tree

    return new_tree