class ArrayStack:
    """LIFO Stack Implementation using a Python list"""

    def __init__(self):
        """Create an empty stack"""
        self._data = []

    def __len__(self):
        """
        :return: the number of elements in the stack
        """
        return len(self._data)

    def is_empty(self):
        """
        :return: True if the stack is empty
        """
        return len(self._data) == 0

    def push(self, e):
        """Add element to top of the stack"""
        self._data.append(e)

    def top(self):
        """
        :return: the element at the top of the stack without removing it
        :raise IndexError exception if the stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]

    def pop(self):
        """
        Remove and return the element from the top of the stack
        :raise IndexError if the stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop() # Remove last item from the list
