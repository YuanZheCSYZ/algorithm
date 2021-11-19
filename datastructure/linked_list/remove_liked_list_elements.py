# 203 https://leetcode.com/problems/remove-linked-list-elements/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Runtime: 64 ms, faster than 88.88% of Python3 online submissions for Remove Linked List Elements.
    Memory Usage: 17.2 MB, less than 26.39% of Python3 online submissions for Remove Linked List Elements.
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        while head and head.val == val:
            head = head.next

        if head:
            p = head.next
            last = head
            while p:
                if p.val == val:
                    last.next = p.next
                else:
                    last = p

                p = p.next

        return head


