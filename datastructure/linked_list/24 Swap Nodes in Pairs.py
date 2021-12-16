# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Runtime: 28 ms, faster than 87.10% of Python3 online submissions for Swap Nodes in Pairs.
    Memory Usage: 14.1 MB, less than 78.37% of Python3 online submissions for Swap Nodes in Pairs.
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        root = head.next
        # !!!
        last = None
        while head and head.next:
            p = head.next
            head.next = p.next
            p.next = head
            if last:
                last.next = p

            last = head
            head = head.next

        return root
