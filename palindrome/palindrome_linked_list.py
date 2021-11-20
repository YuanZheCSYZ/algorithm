# 234 https://leetcode.com/problems/palindrome-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Runtime: 840 ms, faster than 50.33% of Python3 online submissions for Palindrome Linked List.
    Memory Usage: 47.4 MB, less than 28.29% of Python3 online submissions for Palindrome Linked List.
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        for x in range(len(values) // 2):
            if values[x] != values[-x - 1]:
                return False

        return True

    """
    Runtime: 848 ms, faster than 46.71% of Python3 online submissions for Palindrome Linked List.
    Memory Usage: 47.3 MB, less than 38.94% of Python3 online submissions for Palindrome Linked List.
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = ""

        while head:
            res += str(head.val)
            head = head.next

        return res == res[::-1]

    """
    Runtime: 744 ms, faster than 90.13% of Python3 online submissions for Palindrome Linked List.
    Memory Usage: 39.3 MB, less than 86.92% of Python3 online submissions for Palindrome Linked List.
    """
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            temp = slow.next
            slow.next, prev, slow = prev, slow, temp
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True

    """
    Runtime: 652 ms, faster than 98.86% of Python3 online submissions for Palindrome Linked List.
    Memory Usage: 31.4 MB, less than 96.00% of Python3 online submissions for Palindrome Linked List.
    https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space
    """
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        # Odd number of ele
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev