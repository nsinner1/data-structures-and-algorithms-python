class Node:
    """
    This is the Node Class
    """

    def __init__(self, value, next_ = None):
        """
        This is my initialize of the Node
        """
        self.value = value
        self.next_ = next_


    def __repr__(self):
        return f'{self.value} : {self.next_}'


    def __str__(self):
        return f'{self.value} : {self.next_}'


class LinkedList:
    """
    This is a class that creates linked lists
    """

    def __init__(self):
        """
        This is my initialize of linked lists
        """
        self.head = None


    def __str__(self):
         return f'head : {self.head}'


    def insert(self, value):
        """
        This function inserts a new value into the linked list
        """

        node = Node(value)
        if self.head is not None:
            node.next_ = self.head
        self.head = node


    def append_val(self, value):
        current = self.head
        while current != None:
            if current.next_ == None:
                newNode = Node(value)
                current.next_ = newNode
            current = current.next_


    def length(self):
	    current = self.head
	    count = 0
	    while current != None:
		    count += 1
		    current = current.next_
	    return count


    def kth_from_start(self, k):
        length = self.length()
        current = self.head
        kth_from_start = length - k
        for k in range(kth_from_start):
	        current = current.next_
        return current.val


ll = LinkedList()
#print(ll)

ll.insert('Saturday')
ll.insert('Friday')
ll.insert('Thursday')
ll.insert('Wednesday')
ll.insert('Tuesday')
ll.insert('Monday')
ll.insert('Sunday')

print(ll.head)





