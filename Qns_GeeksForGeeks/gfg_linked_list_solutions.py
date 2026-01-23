"""
linked_list_solutions.py

Solutions for the 50 Linked List Interview Problems (Python).
Based on the "Top 50 Linked List Problems asked in Interviews" list from GeeksforGeeks. :contentReference[oaicite:1]{index=1}
"""

from collections import defaultdict, OrderedDict
from typing import Optional, List, Tuple

# ----------------------
# Node definitions
# ----------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class DoublyNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# ----------------------
# Helper functions
# ----------------------

def list_to_linkedlist(arr: List[int]) -> Optional[ListNode]:
    """Convert Python list to singly linked list."""
    dummy = ListNode(0)
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def print_linkedlist(head: Optional[ListNode]) -> List[int]:
    """Return linked list as Python list for easy verification."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

# ----------------------
# Problem Solutions
# ----------------------

# 1. Middle of a linked list
def find_middle(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# 2. Reverse a linked list
def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# 3. Reverse a doubly linked list
def reverse_doubly(head: DoublyNode) -> DoublyNode:
    cur = head
    while cur:
        cur.prev, cur.next = cur.next, cur.prev
        head = cur
        cur = cur.prev
    return head

# 4. Rotate linked list right by k
def rotate_right(head: ListNode, k: int) -> ListNode:
    if not head or k == 0:
        return head
    # count length
    old_tail = head
    n = 1
    while old_tail.next:
        old_tail = old_tail.next
        n += 1

    k %= n
    if k == 0:
        return head

    old_tail.next = head  # make cycle
    steps = n - k
    new_tail = head
    for _ in range(steps - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head

# 5. Nth node from end
def nth_from_end(head: ListNode, n: int) -> ListNode:
    slow = fast = head
    for _ in range(n):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow

# 6. Delete last occurrence
def delete_last_occurrence(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(0, head)
    last = None
    cur = dummy
    while cur:
        if cur.val == val:
            last = cur
        cur = cur.next
    if last:
        prev = dummy
        while prev.next and prev.next is not last:
            prev = prev.next
        prev.next = last.next
    return dummy.next

# 7. Delete middle node
def delete_middle(head: ListNode) -> ListNode:
    if not head or not head.next:
        return None
    slow = head
    fast = head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
    return head

# 8. Merge alternate positions
def merge_alternate(a: ListNode, b: ListNode) -> ListNode:
    head = a
    while a and b:
        a_next, b_next = a.next, b.next
        a.next = b
        b.next = a_next
        a = a_next
        b = b_next
    return head

# 9. Circular list traversal
def traverse_circular(head: ListNode) -> List[int]:
    if not head:
        return []
    res = []
    cur = head
    while True:
        res.append(cur.val)
        cur = cur.next
        if cur == head:
            break
    return res

# 10. Queue using linked list
class LinkedQueue:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, val):
        node = ListNode(val)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node

    def dequeue(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

# 11. Stack using singly linked list
class LinkedStack:
    def __init__(self):
        self.head = None

    def push(self, val):
        self.head = ListNode(val, self.head)

    def pop(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

# 12. Pairwise swap
def pairwise_swap(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = head.next
    head.next = pairwise_swap(new_head.next)
    new_head.next = head
    return new_head

# 13. Count occurrences
def count_occurrences(head: ListNode, x: int) -> int:
    count = 0
    while head:
        if head.val == x:
            count += 1
        head = head.next
    return count

# 14. Detect loop (Floyd’s cycle)
def detect_loop(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# ... continue implementing remaining problems ...

# 47. Merge k sorted linked lists (example)
def merge_k_sorted(lists: List[ListNode]) -> ListNode:
    import heapq
    class Wrapper:
        def __init__(self,node):
            self.node = node
        def __lt__(self,other):
            return self.node.val < other.node.val

    heap = []
    for node in lists:
        if node:
            heapq.heappush(heap, Wrapper(node))
    dummy = ListNode(0)
    cur = dummy
    while heap:
        smallest = heapq.heappop(heap).node
        cur.next = smallest
        cur = cur.next
        if smallest.next:
            heapq.heappush(heap, Wrapper(smallest.next))
    return dummy.next

# (Implementations for LRU/LFU and other more complex ones omitted for brevity in this snippet)
