# Python Stack Implementation - Examples with Definitions

```python
class Stack:
    def __init__(self):
        self.items = []

    # push(item): Add item to the top of the stack
    def push(self, item):
        self.items.append(item)

    # pop(): Remove and return the top item; raises IndexError if empty
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    # peek(): Return the top item without removing it
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    # is_empty(): Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # size(): Return the number of items in the stack
    def size(self):
        return len(self.items)

# Example usage
stack = Stack()
print("Is stack empty?", stack.is_empty())  # True

stack.push(10)
stack.push(20)
stack.push(30)
print("Stack size:", stack.size())  # 3

print("Top element:", stack.peek())  # 30

print("Pop:", stack.pop())  # 30
print("Pop:", stack.pop())  # 20
print("Stack size after pops:", stack.size())  # 1

print("Is stack empty?", stack.is_empty())  # False
