# 160 https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Runtime: 164 ms, faster than 64.98% of Python3 online submissions for Intersection of Two Linked Lists.
    Memory Usage: 29.6 MB, less than 36.51% of Python3 online submissions for Intersection of Two Linked Lists.
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        m = 0
        n = 0

        pA = headA
        pB = headB
        while pA and pB:
            m += 1
            n += 1
            pA = pA.next
            pB = pB.next

        while pA:
            m += 1
            pA = pA.next

        while pB:
            n += 1
            pB = pB.next

        pA = headA
        pB = headB

        if m < n:
            for _ in range(n - m):
                pB = pB.next
        elif n < m:
            for _ in range(m - n):
                pA = pA.next

        while pA != pB:
            pA = pA.next
            pB = pB.next

        if pA:
            return pA

    """
    Runtime: 160 ms, faster than 78.43% of Python3 online submissions for Intersection of Two Linked Lists.
    Memory Usage: 29.4 MB, less than 54.83% of Python3 online submissions for Intersection of Two Linked Lists.
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        LA...xxLB.xx
        LB.xxLA...xx
        :param headA:
        :param headB:
        :return:
        """
        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a