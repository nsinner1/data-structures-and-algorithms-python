from linked_list.linked_list import LinkedList

def test_LinkedList():
    assert LinkedList


def test_append_val():
    linkedlist = LinkedList()
    linkedlist.insert(0)
    assert str(linkedlist) == "{ 0 } -> { 1 } -> NULL"