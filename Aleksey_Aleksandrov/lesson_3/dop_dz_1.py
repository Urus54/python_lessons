# 237. Delete Node in a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

# Accepted
# Runtime: 42 ms
# Your input
# [4,5,1,9]
# 5
# Output
# [4,1,9]
# Expected
# [4,1,9]