class Node:

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_ 


class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top:
            wanted = self.top
            self.top = self.top.next
            wanted.next = None
            return wanted.value

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def peek(self):
        if self.top is None:
            raise AttributeError('The stack is empty')
        else:
            return self.top.value


class Queue:

    def __init__(self):
        self.front = None 

    def enqueue(self, value):
        self.front = Node(value, self.front)

    def dequeue(self):
        if self.front:
            wanted = self.front
            self.front = self.front.next
            wanted.next = None
            return wanted.value

    def peek(self):
        if self.front is None:
            raise AttributeError('The queue is empty')
        else:
            return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False


class PseudoQueue:

    def __init__(self):
        self.add = Stack()
        self.remove = Stack()

    def enqueue(self, value):
	    while self.remove.peek():
		    self.add.push(self.remove.pop())
	
	    self.add.push(value)
	    return self.add.top.value

    def dequeue(self):
	    while self.add.peek():
		    self.remove.push(self.add.pop())
	    return self.remove.pop()
