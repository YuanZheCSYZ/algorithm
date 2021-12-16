# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Runtime: 20 ms, faster than 99.84% of Python3 online submissions for Remove Nth Node From End of List.
    Memory Usage: 14.1 MB, less than 77.36% of Python3 online submissions for Remove Nth Node From End of List.
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        for _ in range(n):
            p = p.next

        # !!!!
        if p is None:
            head = head.next
        else:
            q = head
            while p.next:
                p = p.next
                q = q.next

            if q.next is None:
                head = None
            else:
                q.next = q.next.next
        return head
