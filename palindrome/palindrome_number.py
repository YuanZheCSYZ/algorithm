# 9 https://leetcode.com/problems/palindrome-number/submissions/

class Solution:
    """
    Runtime: 48 ms, faster than 96.17% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14.2 MB, less than 50.87% of Python3 online submissions for Palindrome Number.
    """
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num_s = str(x)
        length = len(num_s)
        for x in range(length // 2):
            if num_s[x] != num_s[-x - 1]:
                return False

        return True

    """
    Runtime: 40 ms, faster than 99.60% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14.3 MB, less than 17.01% of Python3 online submissions for Palindrome Number.
    """
    def isPalindrome2(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False