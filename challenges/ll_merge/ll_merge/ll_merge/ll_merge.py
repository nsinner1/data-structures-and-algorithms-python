class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def print_link_list(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next 


def ll_merge(list1, list2):
    head = ptr = Node()
    while list1 or list2:
        if list1 and (not list2 or list1.data <= list2.data):
            ptr.next = Node(list1.data)
            list1 = list1.next
        else:
            ptr.next = Node(list2.data)
            list2 = list2.next
        ptr = ptr.next
    return head.next 


LL1 = LinkedList()
LL1.insert(2)
LL1.insert(4)
LL1.insert(6)
LL1.insert(8)

LL2 = LinkedList()
LL2.insert(1)
LL2.insert(3)
LL2.insert(5)
LL2.insert(7)

LL3 = LinkedList()
LL3.head = ll_merge(LL1.head, LL2.head)
LL3.print_link_list()
