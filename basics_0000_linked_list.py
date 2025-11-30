"""
A linked list is a linear data structure composed of a sequence of nodes, where each node contains data and a reference
(or "pointer") to the next node in the sequence.
Unlike Python's built-in list type (which is a dynamic array), linked lists do not store elements in contiguous memory
locations, making them more efficient for insertions and deletions at the beginning of the list.
Key Concepts
Node: The basic building block of a linked list. Each node typically has two parts: the data (the value it stores) and a
 next pointer (a reference to the next node in the list).
Head: The first node in the linked list. The entire list can be accessed by starting at the head and following the next pointers.
Traversal: The process of visiting each node in the linked list, typically starting from the head and moving from one
node to the next until the end is reached (where the next pointer is None).

"""

"""✅ Linked List in Python — Methods & Explanations

We’ll cover: Core Methods

1. append()
    10 → 20 → 30 → None
    10 → 20 → 30 → 40 → None

2. prepend()
    10 → 20 → 30 → None
    5 → 10 → 20 → 30 → None

3. insert()
    10 → 20 → 30 → 40 → None
    10 → 20 → 25 → 30 → 40 → None

4. delete()
    10 → 20 → 30 → 40 → None
    10 → 20 → 40 → None

5. search()
    10 → 20 → 30 → None

6. reverse()
    10 → 20 → 30 → 40 → None
    10 ← 20 ← 30 ← 40

7. length()
    10 → 20 → 30 → None
    Length = 3

8. to_list() (convert to Python list)
    10 → 20 → 30 → None
    [10, 20, 30]

display()

Let’s start!"""

# 📌 Node + LinkedList Base Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

# 1️⃣ append(value) — Insert at end
# Use: Add an element to the tail of the list.

def append(self, data):
    new_node = Node(data)
    if not self.head:            # If list is empty
        self.head = new_node
        return

    temp = self.head
    while temp.next:
        temp = temp.next         # Go to last node
    temp.next = new_node         # Add new node at end


# ✔ Time: O(n)
# ✔ Why: Must traverse to end.
# 2️⃣ prepend(value) — Insert at front
# Use: Add element at beginning.

def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head  # Point new node to old head
    self.head = new_node       # Update head


✔ Time: O(1)

# 3️⃣ insert(index, value) — Insert at specific position
# Use: Insert anywhere in list.

def insert(self, index, data):
    if index == 0:
        self.prepend(data)
        return

    new_node = Node(data)
    temp = self.head
    count = 0

    while temp and count < index - 1:
        temp = temp.next
        count += 1

    if not temp:
        raise IndexError("Index out of range")

    new_node.next = temp.next
    temp.next = new_node


# ✔ Time: O(n)
# 4️⃣ delete(value) — Delete first occurrence
# Use: Remove a node by value.

def delete(self, key):
    temp = self.head

    # Case 1: deleting head
    if temp and temp.data == key:
        self.head = temp.next
        return

    # Case 2: search for node
    prev = None
    while temp and temp.data != key:
        prev = temp
        temp = temp.next

    if not temp:                  # Not found
        return

    prev.next = temp.next         # Bypass deleted node


✔ Time: O(n)

5️⃣ search(value) — Find if value exists
def search(self, key):
    temp = self.head
    while temp:
        if temp.data == key:
            return True
        temp = temp.next
    return False


✔ Time: O(n)

6️⃣ reverse() — Reverse linked list
def reverse(self):
    prev = None
    curr = self.head

    while curr:
        nxt = curr.next      # store next
        curr.next = prev     # reverse link
        prev = curr          # move prev
        curr = nxt           # move curr

    self.head = prev


✔ Time: O(n)
✔ Space: O(1)

7️⃣ length() — Count nodes
def length(self):
    count = 0
    temp = self.head
    while temp:
        count += 1
        temp = temp.next
    return count


✔ Time: O(n)

8️⃣ to_list() — Convert to Python list
def to_list(self):
    arr = []
    temp = self.head
    while temp:
        arr.append(temp.data)
        temp = temp.next
    return arr


✔ Useful for debugging and testing.

9️⃣ display() — Print linked list
def display(self):
    temp = self.head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

📦 Complete LinkedList Class

Here is everything together:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        temp = self.head
        count = 0
        while temp and count < index - 1:
            temp = temp.next
            count += 1
        if not temp:
            raise IndexError("Index out of range")
        new_node.next = temp.next
        temp.next = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            return
        prev.next = temp.next

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def to_list(self):
        arr = []
        temp = self.head
        while temp:
            arr.append(temp.data)
            temp = temp.next
        return arr

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



"""Below are clean, clear, fully working Python implementations of:
✔️ Singly Linked List
✔️ Doubly Linked List
✔️ Circular Linked List

Each includes: insert, delete, search, print, etc."""

# 🟩 1. Singly Linked List — Python Implementation
# Each node has only next → pointer.
"""
10 → 20 → 30 → 40 → None

+------+      +------+      +------+      +------+
| 10   | ---> | 20   | ---> | 30   | ---> | 40   |
+------+      +------+      +------+      +------+
     next         next          next          next → None
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        if not self.head:
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next and temp.next.data != key:
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# 🟦 2. Doubly Linked List — Python Implementation
# Each node has prev ← and next → pointers.
"""
10 ⇄ 20 ⇄ 30 ⇄ 40
    prev         prev         prev         prev
     ↓            ↓            ↓            ↓
None ←+------+←→+------+←→+------+←→+------+→ None
     | 10   |   | 20   |   | 30   |   | 40   |
     +------+→→+------+→→+------+→→+------+
            next        next        next
"""

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_at_begin(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, key):
        if not self.head:
            return

        temp = self.head

        # delete head
        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        while temp and temp.data != key:
            temp = temp.next

        if not temp:
            return

        # unlink node
        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    def print_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def print_backward(self):
        temp = self.head
        if not temp:
            return

        # Go to tail
        while temp.next:
            temp = temp.next

        # Print backward
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# 🟨 3. Circular Linked List — Python Implementation
# Last node points back to head, forming a circle.
"""
10 → 20 → 30 → (back to 10)
             +------+
             | 10   |
             +------+
                ↓ next
             +------+
             | 20   |
             +------+
                ↓ next
             +------+
             | 30   |
             +------+
                ↓ next
                back to 10
                ↖───────────┘

Complete circle:
10 → 20 → 30 → 10 → 20 → 30 → ...

"""


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def delete(self, key):
        if not self.head:
            return

        curr = self.head
        prev = None

        # case 1: deleting head
        if curr.data == key:
            if curr.next == self.head:  # only one node
                self.head = None
                return

            # find last node
            while curr.next != self.head:
                curr = curr.next

            curr.next = self.head.next
            self.head = self.head.next
            return

        # deleting non-head
        curr = self.head
        while curr.next != self.head:
            prev = curr
            curr = curr.next
            if curr.data == key:
                prev.next = curr.next
                return

    def print_list(self):
        if not self.head:
            print("Empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")
