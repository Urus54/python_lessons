# 876. Middle of the Linked List


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow,fast=head,head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        return slow

# Accepted
# Runtime: 42 ms
# Your input
# [1,2,3,4,5]
# Output
# [3,4,5]
# Expected
# [3,4,5]