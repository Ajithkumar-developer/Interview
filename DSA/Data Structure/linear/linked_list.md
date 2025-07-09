# Python Linked List Implementation - Examples with Definitions

```python
# Node class: Represents each element in the list
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node

# LinkedList class: Manages the nodes
class LinkedList:
    def __init__(self):
        self.head = None  # Start of the list

    # insert_at_end(): Adds a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # insert_at_beginning(): Adds a node at the start
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # delete_node(): Deletes the first node with the given value
    def delete_node(self, key):
        curr = self.head

        if curr is not None and curr.data == key:
            self.head = curr.next
            curr = None
            return

        prev = None
        while curr is not None and curr.data != key:
            prev = curr
            curr = curr.next

        if curr is None:
            return  # Key not found

        prev.next = curr.next
        curr = None

    # search(): Returns True if key is found
    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    # print_list(): Prints all node values
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Example usage
ll = LinkedList()

# Insert elements
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_beginning(5)
ll.insert_at_end(30)

print("Linked List after insertions:")
ll.print_list()  # 5 -> 10 -> 20 -> 30 -> None

# Delete a node
ll.delete_node(20)
print("After deleting 20:")
ll.print_list()  # 5 -> 10 -> 30 -> None

# Search for elements
print("Search 10:", ll.search(10))  # True
print("Search 100:", ll.search(100))  # False
