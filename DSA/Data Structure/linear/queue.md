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
