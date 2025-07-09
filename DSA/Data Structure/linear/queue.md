# Python Queue Implementation - Examples with Definitions

```python
class Queue:
    def __init__(self):
        self.items = []

    # enqueue(item): Add item to the end of the queue
    def enqueue(self, item):
        self.items.append(item)

    # dequeue(): Remove and return item from the front; raises IndexError if empty
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    # peek(): Return the front item without removing it
    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    # is_empty(): Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # size(): Return the number of items in the queue
    def size(self):
        return len(self.items)

# Example usage
queue = Queue()
print("Is queue empty?", queue.is_empty())  # True

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Queue size:", queue.size())  # 3

print("Front element:", queue.peek())  # 10

print("Dequeue:", queue.dequeue())  # 10
print("Dequeue:", queue.dequeue())  # 20
print("Queue size after dequeues:", queue.size())  # 1

print("Is queue empty?", queue.is_empty())  # False
```

# Python Queue Implementation Using Linked List - Examples with Definitions

```python
# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class using linked list
class Queue:
    def __init__(self):
        self.front = None  # Points to the front node
        self.rear = None   # Points to the rear node

    # is_empty(): Check if queue is empty
    def is_empty(self):
        return self.front is None

    # enqueue(item): Add item to the rear of the queue
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            # Queue is empty
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    # dequeue(): Remove and return item from the front of the queue
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        temp = self.front
        self.front = temp.next
        # If queue becomes empty, update rear to None
        if self.front is None:
            self.rear = None
        return temp.data

    # peek(): Return front item without removing
    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    # size(): Return number of items (O(n) operation)
    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    # print_queue(): Print all elements in queue
    def print_queue(self):
        current = self.front
        while current:
            print(current.data, end=" <- ")
            current = current.next
        print("None")

# Example usage
q = Queue()
print("Is queue empty?", q.is_empty())  # True

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue after enqueues:")
q.print_queue()  # 10 <- 20 <- 30 <- None

print("Front element:", q.peek())  # 10

print("Dequeue:", q.dequeue())  # 10
print("Dequeue:", q.dequeue())  # 20

print("Queue after dequeues:")
q.print_queue()  # 30 <- None

print("Queue size:", q.size())  # 1

print("Is queue empty?", q.is_empty())  # False

print("Dequeue:", q.dequeue())  # 30
print("Is queue empty after all dequeues?", q.is_empty())  # True

# Trying to dequeue from empty queue raises error:
# q.dequeue()  # IndexError: dequeue from empty queue
