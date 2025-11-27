???

"""
Problem:

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, and each node contains a single digit.

Add the two numbers and return the sum as a linked list, also in reverse order.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next

# l1 = [2,4,3] represents the number 342
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# l2 = [5,6,4] represents the number 465
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(addTwoNumbers(l1,l2))
print(addTwoNumbers(l1,l2))