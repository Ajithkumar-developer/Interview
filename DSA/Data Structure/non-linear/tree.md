# Python Binary Tree Implementation - Examples with Definitions

```python
# Node class for binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# BinaryTree class with insert and traversal methods
class BinaryTree:
    def __init__(self):
        self.root = None

    # insert(): Insert node in level-order
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if not temp.left:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)
            if not temp.right:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    # inorder(): Left -> Root -> Right
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # preorder(): Root -> Left -> Right
    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # postorder(): Left -> Right -> Root
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    # level_order(): Breadth-first traversal
    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            print(temp.data, end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

# Example usage
bt = BinaryTree()
for value in [1, 2, 3, 4, 5, 6]:
    bt.insert(value)

# Tree structure after inserts (Level order):
#          1
#        /   \
#       2     3
#      / \   /
#     4   5 6

print("Inorder Traversal:")
bt.inorder(bt.root)  # 4 2 5 1 6 3

print("\nPreorder Traversal:")
bt.preorder(bt.root)  # 1 2 4 5 3 6

print("\nPostorder Traversal:")
bt.postorder(bt.root)  # 4 5 2 6 3 1

print("\nLevel Order Traversal:")
bt.level_order()  # 1 2 3 4 5 6
```

# Python Binary Search Tree (BST) Implementation - Examples with Definitions

```python
# Node class for BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# BST class with common operations
class BST:
    def __init__(self):
        self.root = None

    # insert(): Add a node in BST
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node  # No duplicates allowed

    # search(): Returns True if data is found
    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    # delete(): Remove a node from BST
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: Get inorder successor
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # inorder(): Left -> Root -> Right
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=' ')
            self._inorder(node.right)

    # preorder(): Root -> Left -> Right
    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print(node.data, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    # postorder(): Left -> Right -> Root
    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data, end=' ')

# Example usage
bst = BST()
for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)

# BST structure:
#         50
#       /    \
#     30      70
#    /  \    /  \
#  20   40  60  80

print("Inorder traversal (sorted):")
bst.inorder()  # 20 30 40 50 60 70 80

print("Preorder traversal:")
bst.preorder()  # 50 30 20 40 70 60 80

print("Postorder traversal:")
bst.postorder()  # 20 40 30 60 80 70 50

print("Search 60:", bst.search(60))  # True
print("Search 100:", bst.search(100))  # False

bst.delete(70)  # Delete node with two children
print("Inorder after deleting 70:")
bst.inorder()  # 20 30 40 50 60 80
```

# Python AVL Tree Implementation (with Insert, Delete, Traversals)

This example implements a **self-balancing AVL Tree** in Python, supporting:

- Insertion
- Deletion
- Inorder Traversal (sorted)
- Preorder Traversal (structure)

---

## ✅ Code

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Rotate
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Rotate
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # No duplicates

        # Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Rebalance
        return self._rebalance(root, key)

    def delete(self, root, key):
        if not root:
            return root

        # Standard BST delete
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Rebalance
        return self._rebalance_after_delete(root)

    def _rebalance(self, root, key):
        balance = self.get_balance(root)

        # Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def _rebalance_after_delete(self, root):
        balance = self.get_balance(root)

        # Left heavy
        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)  # LL
            else:
                root.left = self.left_rotate(root.left)  # LR
                return self.right_rotate(root)

        # Right heavy
        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)  # RR
            else:
                root.right = self.right_rotate(root.right)  # RL
                return self.left_rotate(root)

        return root

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)


# Example usage
tree = AVLTree()
root = None

# Insert nodes
for val in [10, 20, 30, 40, 50, 25]:
    root = tree.insert(root, val)

print("Inorder traversal (sorted):")
tree.inorder(root)  # Output: 10 20 25 30 40 50

print("\nPreorder traversal (shows structure):")
tree.preorder(root)  # Output: 30 20 10 25 40 50

# Delete a node
root = tree.delete(root, 20)
print("\n\nInorder after deleting 20:")
tree.inorder(root)  # Output: 10 25 30 40 50

print("\nPreorder after deleting 20:")
tree.preorder(root)  # Shows balanced structure

bst.delete(20)  # Delete leaf node
print("Inorder after deleting 20:")
bst.inorder()  # 30 40 50 60 80
```

