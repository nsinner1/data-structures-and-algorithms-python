from linked_list.linked_list import Node, LinkedList

def test_empty_linked_list():
    linked_list = LinkedList()
    assert linked_list.head == None

def test_Node_created():
    assert 3 == Node(3).value
    assert None == Node(3).next

def test_insert_to_empty():
    val = 5
    linked_list = LinkedList()
    linked_list.insert(val)
    assert linked_list.head.value == 5

def test_head_to_the_first_el():
   linked_list = LinkedList()
   linked_list.insert('a')
   assert linked_list.head.value == 'a'
   linked_list.insert('b')
   assert linked_list.head.value == 'b'
   linked_list.insert('c')
   assert linked_list.head.value == 'c'
   linked_list.insert('d')
   assert linked_list.head.value == 'd'
   assert linked_list.head.next.next.value == 'b'



