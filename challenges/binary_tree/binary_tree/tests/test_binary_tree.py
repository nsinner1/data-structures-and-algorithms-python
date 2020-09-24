from binary_tree.binary_tree import _Node, BinarySearchTree, BinaryTree, Queue
import pytest

@pytest.fixture
def my_bst():
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(11)
    tree.add(13)
    tree.add(7)
    tree.add(8)
    tree.add(5)
    tree.add(19)
    tree.add(17)
    tree.add(23)


    return tree

def test_tree_instance():
    tree = BinaryTree()
    assert tree._root is None

def test_tree_one_member():
    tree = BinarySearchTree()
    tree.add('apples')
    assert tree._root.value == 'apples'

def test_add_three_members():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree._root.value == 10
    assert tree._root.left.value == 5
    assert tree._root.right.value == 15
