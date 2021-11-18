# 141 https://leetcode.com/problems/linked-list-cycle/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Runtime: 1284 ms, faster than 5.06% of Python3 online submissions for Linked List Cycle.
    Memory Usage: 17.7 MB, less than 25.62% of Python3 online submissions for Linked List Cycle.
    O(N^2)
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        while head:
            if not head:
                return False

            if head in visited:
                return True

            visited.append(head)
            head = head.next

        return False

    """
    Runtime: 52 ms, faster than 83.29% of Python3 online submissions for Linked List Cycle.
    Memory Usage: 17.6 MB, less than 56.96% of Python3 online submissions for Linked List Cycle.
    O(N)
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False