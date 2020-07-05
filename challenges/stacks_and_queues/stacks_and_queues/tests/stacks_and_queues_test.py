import pytest 

from stacks_and_queues.stacks_and_queues import Stack, Queue

class TestStack:

    @pytest.fixture()
    def stack(self):
        return Stack()

    def test_instantiation_empty(self):
        assert Stack()

    def test_push(self, stack):
        assert stack.top is None

        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)

        assert stack.top.value == 5
        assert stack.top.next.value == 4
        assert stack.top.next.next.value == 3
        assert stack.top.next.next.next.value == 2
        assert stack.top.next.next.next.next.value == 1

    def test_pop(self, stack):
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)

        assert stack.pop() == 4
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.top is None

    def test_peek(self, stack):
        stack.push(1)
        assert stack.peek() == 1
        stack.push(2)
        assert stack.peek() == 2
        stack.push(3)
        assert stack.peek() == 3
        stack.push(4)
        assert stack.peek() == 4


class TestQueue:

    @pytest.fixture()
    def queue(self):
        return Queue()

    def test_instantiation_empty(self):
        assert Queue()
