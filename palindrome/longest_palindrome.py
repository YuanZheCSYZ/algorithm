# 409 https://leetcode.com/problems/longest-palindrome

class Solution(object):

    """
    Runtime: 28 ms, faster than 37.83% of Python online submissions for Longest Palindrome.
    Memory Usage: 13.3 MB, less than 91.24% of Python online submissions for Longest Palindrome.
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnter = collections.Counter(s)
        odd = False
        res = 0
        for x in cnter:
            cnt = cnter[x]
            if cnt % 2:
                odd = True
                res += cnt - 1
            else:
                res += cnt

        if odd:
            res += 1

        return res

    """
    Runtime: 28 ms, faster than 37.83% of Python online submissions for Longest Palindrome.
    Memory Usage: 13.3 MB, less than 91.24% of Python online submissions for Longest Palindrome.
    https://leetcode.com/problems/longest-palindrome/discuss/89587/What-are-the-odds-(Python-and-C%2B%2B)
    """
    def longestPalindrome(self, s):
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)