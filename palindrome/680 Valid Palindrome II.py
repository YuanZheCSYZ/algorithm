# 680 https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    """
    Runtime: 88 ms, faster than 94.96% of Python3 online submissions for Valid Palindrome II.
    Memory Usage: 14.7 MB, less than 40.60% of Python3 online submissions for Valid Palindrome II.
    """
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        for x in range(n // 2):
            if s[x] != s[n - x - 1]:
                rm_left = s[x + 1:n - x]
                if rm_left == rm_left[::-1]:
                    return True

                rm_right = s[x:n - 1 - x]
                return rm_right == rm_right[::-1]

        return True