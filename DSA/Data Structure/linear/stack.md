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
```

# Python Stack Implementation Using Linked List - Examples with Definitions

```python
# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class using linked list
class Stack:
    def __init__(self):
        self.top = None  # Points to the top node

    # is_empty(): Check if stack is empty
    def is_empty(self):
        return self.top is None

    # push(item): Add item to the top of the stack
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    # pop(): Remove and return the top item; raises IndexError if empty
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    # peek(): Return the top item without removing it
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    # size(): Return number of items (O(n) operation)
    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

    # print_stack(): Print all elements from top to bottom
    def print_stack(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
stack = Stack()
print("Is stack empty?", stack.is_empty())  # True

stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after pushes:")
stack.print_stack()  # 30 -> 20 -> 10 -> None

print("Top element:", stack.peek())  # 30

print("Pop:", stack.pop())  # 30
print("Pop:", stack.pop())  # 20

print("Stack after pops:")
stack.print_stack()  # 10 -> None

print("Stack size:", stack.size())  # 1

print("Is stack empty?", stack.is_empty())  # False

print("Pop:", stack.pop())  # 10
print("Is stack empty after all pops?", stack.is_empty())  # True

# Trying to pop from empty stack raises error:
# stack.pop()  # IndexError: pop from empty stack

