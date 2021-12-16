# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    """
    Runtime: 1300 ms, faster than 47.81% of Python3 online submissions for Longest Palindromic Substring.
    Memory Usage: 14.1 MB, less than 99.01% of Python3 online submissions for Longest Palindromic Substring.
    """
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        m = 1
        n = len(s)
        res = s[0]
        for i in range(1, n):
            j = 0
            while 0 <= i - 1 - j and i + j < n:
                if s[i - 1 - j] != s[i + j]:
                    break

                if m < j * 2 + 2:
                    m = j * 2 + 2
                    res = s[i - 1 - j: i + j + 1]

                j += 1

            j = 1
            while 0 <= i - j and i + j < n:
                if s[i - j] != s[i + j]:
                    break

                if m < j * 2 + 1:
                    m = j * 2 + 1
                    res = s[i - j: i + j + 1]

                j += 1

        return res

    """
    Runtime: 100 ms, faster than 98.78% of Python3 online submissions for Longest Palindromic Substring.
    Memory Usage: 14.2 MB, less than 81.70% of Python3 online submissions for Longest Palindromic Substring.
    https://leetcode.com/problems/longest-palindromic-substring/discuss/2925/Python-O(n2)-method-with-some-optimization-88ms.
    """
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        maxLen = 1
        start = 0
        for i in range(len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start:start + maxLen]
