# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Runtime: 60 ms, faster than 96.67% of Python3 online submissions for Add Two Numbers.
    Memory Usage: 14.1 MB, less than 91.23% of Python3 online submissions for Add Two Numbers.
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = l1
        carry = 0
        p = l1
        while l1 and l2:
            carry += l1.val + l2.val
            l1.val = carry % 10
            carry //= 10

            p = l1
            l1 = l1.next
            l2 = l2.next

        if l2:
            p.next = l2
            l1 = l2

        while carry and l1:
            carry += l1.val
            l1.val = carry % 10
            carry //= 10

            p = l1
            l1 = l1.next

        if carry:
            p.next = ListNode(carry)

        return root

    """
    Runtime: 56 ms, faster than 99.10% of Python3 online submissions for Add Two Numbers.
    Memory Usage: 14.2 MB, less than 73.55% of Python3 online submissions for Add Two Numbers.
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = l1
        carry = 0
        while l1 or l2:
            carry += l1.val
            if l2:
                carry += l2.val
                l2 = l2.next

            l1.val = carry % 10
            carry //= 10

            if l1.next is None:
                if l2:
                    l1.next = l2
                    l2 = None
                else:
                    if carry:
                        l1.next = ListNode(carry)
                        break

            l1 = l1.next

        return root