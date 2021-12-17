# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Runtime: 39 ms, faster than 52.01% of Python3 online submissions for Rotate List.
    Memory Usage: 14.2 MB, less than 86.00% of Python3 online submissions for Rotate List.
    """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n = 2
        p = head
        q = head.next
        while q.next:
            p = p.next
            q = q.next
            n += 1

        k %= n
        if k:
            q.next = head
            # This is rotating one
            head = q
            k = (n - k + 1) % n
            while k:
                head = head.next
                p = p.next
                k -= 1

            p.next = None

        return head
