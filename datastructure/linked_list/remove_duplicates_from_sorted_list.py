# 83 https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Runtime: 40 ms, faster than 82.55% of Python3 online submissions for Remove Duplicates from Sorted List.
    Memory Usage: 14.3 MB, less than 58.46% of Python3 online submissions for Remove Duplicates from Sorted List.
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        current = head.val
        last = head
        p = head.next
        while p:
            if p.val == current:
                last.next = p.next
            else:
                last = p
                current = p.val

            p = p.next

        return head